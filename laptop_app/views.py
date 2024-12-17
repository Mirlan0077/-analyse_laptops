from django.http import JsonResponse
from .laptop_analysis import LaptopAnalysis
from django.shortcuts import render


def about(request):
    return render(request, 'about.html')

def analyze_laptops(request):
    # Создаем объект анализа
    analyzer = LaptopAnalysis()

    # Получаем топ-10 и низ-10 ноутбуков
    top_10_laptops = analyzer.get_top_10_laptops()
    low_10_laptops = analyzer.get_low_10_laptops()

    # Форматируем данные для ответа (например, получаем нужные атрибуты)
    top_10_data = [
        {
            'name': laptop.name,
            'brand': laptop.brand,
            'price': laptop.price,
            'year': laptop.year,
            'rating': laptop.rating
        }
        for laptop in top_10_laptops
    ]

    low_10_data = [
        {
            'name': laptop.name,
            'brand': laptop.brand,
            'price': laptop.price,
            'year': laptop.year,
            'rating': laptop.rating
        }
        for laptop in low_10_laptops
    ]

    # Объединяем данные
    response_data = {
        'top_10_laptops': top_10_data,
        'low_10_laptops': low_10_data
    }

    # Возвращаем красиво отформатированный JSON
    return JsonResponse(response_data, json_dumps_params={'indent': 4})