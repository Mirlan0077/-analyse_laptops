from django.http import JsonResponse

from .laptop_analysis import LaptopAnalysis
from .models import Laptop

from .utils.csv_processor import process_csv


def analyze_laptops(request):


    # Получаем ноутбуки из базы данных и обновляем их рейтинг
    laptops = Laptop.objects.all()  # Получаем все ноутбуки
    for laptop in laptops:
        laptop.save()  # Обновляем рейтинг для каждого ноутбука (с использованием метода calculate_score)

    # Получаем топ-10 и низ-10 ноутбуков по рейтингу
    top_10_laptops = Laptop.objects.order_by('-rating')[:10]
    low_10_laptops = Laptop.objects.order_by('rating')[:10]

    # Создаем экземпляр анализа с OpenAI API
    openai_api_key = "YOUR_API_KEY"  # Замените на ваш API-ключ OpenAI
    analyzer = LaptopAnalysis(openai_api_key)

    # Получаем данные из OpenAI
    openai_data = analyzer.analyze_in_parallel()

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
        'openai_data': openai_data  # Добавляем данные из OpenAI
    }

    return JsonResponse(response_data, json_dumps_params={'indent': 4})


def upload_csv_and_analyze(request):
    """Обработка файла CSV, загрузка данных в базу и анализ ноутбуков."""
    file_path = 'laptop_app/fixtures/mindfactory_done.csv'  # Замените на путь к вашему файлу
    process_csv(file_path)  # Загрузка данных из CSV

    laptops = Laptop.objects.all()
    for laptop in laptops:
        laptop.save()  # Обновляем рейтинг для каждого ноутбука

    # Получаем топ-10 и низ-10 ноутбуков по рейтингу
    top_10_laptops = Laptop.objects.order_by('-rating')[:10]
    low_10_laptops = Laptop.objects.order_by('rating')[:10]

    # Создаем экземпляр анализа с OpenAI API
    openai_api_key = "YOUR_API_KEY"  # Замените на ваш API-ключ OpenAI
    analyzer = LaptopAnalysis(openai_api_key)

    # Получаем данные из OpenAI
    openai_data = analyzer.analyze_in_parallel()

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
        'openai_data': openai_data  # Добавляем данные из OpenAI
    }

    return JsonResponse(response_data, json_dumps_params={'indent': 4})
