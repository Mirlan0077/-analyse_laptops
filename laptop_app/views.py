from django.http import JsonResponse
from .models import Laptop
from .utils.csv_processor import process_csv

def analyze_laptops(request):

    top_10_laptops = Laptop.objects.order_by('-rating')[:10]
    low_10_laptops = Laptop.objects.order_by('rating')[:10]

    def format_laptops(laptops):
        return [
            {
                'name': laptop.name,
                'brand': laptop.category,
                'model': laptop.cpu_processor,
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

    file_path = 'laptop_app/fixtures/mindfactory_done.csv'
    process_csv(file_path)


    valid_laptops = Laptop.objects.filter(rating__gt=0).order_by('-rating')

    top_10_laptops = valid_laptops[:10]
    low_10_laptops = valid_laptops.reverse()[:10]


    def format_laptops(laptops):
        return [
            {
                'name': laptop.name,
                'brand': laptop.category,
                'model': laptop.cpu_processor,
                'rating': laptop.rating
            }
            for laptop in laptops
        ]

    response_data = {
        'top_10_laptops': format_laptops(top_10_laptops),
        'low_10_laptops': format_laptops(low_10_laptops),
    }

    return JsonResponse(response_data, json_dumps_params={'indent': 4})
