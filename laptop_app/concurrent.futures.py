import concurrent.futures
from laptop_app.models import Laptop


class LaptopAnalysis:
    def __init__(self):
        self.laptops = Laptop.objects.all()

    def analyze_in_parallel(self):
        top_10 = self.get_top_10_laptops()
        low_10 = self.get_low_10_laptops()

        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [
                executor.submit(self.get_manufacturers, top_10),
                executor.submit(self.get_manufacturers, low_10)
            ]
            top_manufacturers, low_manufacturers = [future.result() for future in futures]

        return {
            'top_10_laptops': list(top_10),
            'low_10_laptops': list(low_10),
            'top_manufacturers': top_manufacturers,
            'low_manufacturers': low_manufacturers
        }

