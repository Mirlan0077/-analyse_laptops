from laptop_app.models import Laptop

class LaptopAnalysis:
    def __init__(self):
        self.laptops = Laptop.objects.all()

    def get_top_10_laptops(self):
        # Сортируем ноутбуки по рейтингу в порядке убывания и берем топ-10
        return self.laptops.filter(rating__isnull=False).order_by('-rating')[:10]

    def get_low_10_laptops(self):
        # Сортируем ноутбуки по рейтингу в порядке возрастания и берем 10 худших
        return self.laptops.filter(rating__isnull=False).order_by('rating')[:10]


    def get_manufacturers(self, laptops):
        # Получаем список производителей ноутбуков
        return {laptop.brand for laptop in laptops}

    def analyze(self):
        top_10 = self.get_top_10_laptops()
        low_10 = self.get_low_10_laptops()
        top_manufacturers = self.get_manufacturers(top_10)
        low_manufacturers = self.get_manufacturers(low_10)

        return {
            'top_10_laptops': [
                {"name": laptop.name, "brand": laptop.brand, "price": laptop.price, "year": laptop.year}
                for laptop in top_10
            ],
            'low_10_laptops': [
                {"name": laptop.name, "brand": laptop.brand, "price": laptop.price, "year": laptop.year}
                for laptop in low_10
            ],
            'top_manufacturers': list(top_manufacturers),
            'low_manufacturers': list(low_manufacturers)
        }
