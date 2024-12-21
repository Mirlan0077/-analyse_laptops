from laptop_app.models import Laptop
import concurrent.futures


class LaptopAnalysis:
    def __init__(self):
        self.laptops = Laptop.objects.all()

    def get_top_10_laptops(self):
        return self.laptops.filter(rating__isnull=False).order_by('-rating')[:10]

    def get_low_10_laptops(self):
        return self.laptops.filter(rating__isnull=False).order_by('rating')[:10]

    def get_manufacturers(self, laptops):
        return {laptop.brand for laptop in laptops}

    def get_all_manufacturers(self):
        return {laptop.brand for laptop in self.laptops}

    def analyze_in_parallel(self):
        self.update_ratings()

        top_10 = self.get_top_10_laptops()
        low_10 = self.get_low_10_laptops()

        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [
                executor.submit(self.get_manufacturers, top_10),
                executor.submit(self.get_manufacturers, low_10),
                executor.submit(self.get_all_manufacturers)
            ]
            top_manufacturers, low_manufacturers, all_manufacturers = [
                future.result() for future in futures
            ]

        return {
            'top_10_laptops': list(top_10),
            'low_10_laptops': list(low_10),
            'top_manufacturers': top_manufacturers,
            'low_manufacturers': low_manufacturers,
            'all_manufacturers': all_manufacturers
        }
