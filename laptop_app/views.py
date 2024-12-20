from django.http import JsonResponse
from .models import Laptop
from .utils.csv_processor import process_csv

def analyze_laptops(request):
    """Анализирует ноутбуки, используя расчет рейтингов с помощью модели Django."""

    # Обновляем рейтинги для всех ноутбуков в базе данных
    laptops = Laptop.objects.all()  # Получаем все ноутбуки
    for laptop in laptops:
        laptop.save()

    # Получаем топ-10 и низ-10 ноутбуков по рейтингу
    top_10_laptops = Laptop.objects.order_by('-rating')[:10]
    low_10_laptops = Laptop.objects.order_by('rating')[:10]

    # Форматируем данные для ответа
    def format_laptops(laptops):
        return [
            {
                'name': laptop.name,
                'brand': laptop.category,  # Используем category как бренд
                'model': laptop.cpu_processor,  # Используем cpu_processor как модель
                'rating': laptop.rating
            }
            for laptop in laptops
        ]

    response_data = {
        'top_10_laptops': format_laptops(top_10_laptops),
        'low_10_laptops': format_laptops(low_10_laptops),
    }

    return JsonResponse(response_data, json_dumps_params={'indent': 4})

def upload_csv_and_analyze(request):
    """Обработка файла CSV, загрузка данных в базу и анализ ноутбуков."""

    # Загрузка данных из CSV
    file_path = 'laptop_app/fixtures/mindfactory_done.csv'  # Замените на путь к вашему файлу
    process_csv(file_path)  # Загрузка данных из CSV

    # Обновляем рейтинги для всех ноутбуков в базе данных
    laptops = Laptop.objects.all()  # Получаем все ноутбуки
    print(f"Total laptops in the database: {len(laptops)}")  # Выводим количество ноутбуков

    # Печатаем несколько ноутбуков для отладки
    for laptop in laptops[:5]:
        print(f"Laptop: {laptop.name}, Rating: {laptop.rating}")

    # Исключаем ноутбуки с рейтингом 0
    valid_laptops = Laptop.objects.filter(rating__gt=0).order_by('-rating')

    # Печатаем количество ноутбуков с рейтингом больше 0
    print(f"Valid laptops with rating > 0: {len(valid_laptops)}")

    # Получаем топ-10 и низ-10 ноутбуков по рейтингу
    top_10_laptops = valid_laptops[:10]
    low_10_laptops = valid_laptops.reverse()[:10]

    print(f"Top 10 laptops: {[laptop.name for laptop in top_10_laptops]}")
    print(f"Low 10 laptops: {[laptop.name for laptop in low_10_laptops]}")

    # Форматируем данные для ответа
    def format_laptops(laptops):
        return [
            {
                'name': laptop.name,
                'brand': laptop.category,  # Используем category как бренд
                'model': laptop.cpu_processor,  # Используем cpu_processor как модель
                'rating': laptop.rating
            }
            for laptop in laptops
        ]

    # Возвращаем топ-10 и низ-10 ноутбуков
    response_data = {
        'top_10_laptops': format_laptops(top_10_laptops),
        'low_10_laptops': format_laptops(low_10_laptops),
    }

    return JsonResponse(response_data, json_dumps_params={'indent': 4})
