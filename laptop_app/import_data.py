import csv
from laptop_app.models import Laptop

def import_laptops_from_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            Laptop.objects.create(
                name=row['name'],
                manufacturer=row['manufacturer'],
                year=int(row['year']),
                rating=float(row['rating']),
                cpu=row['cpu'],
                ram=int(row['ram']),
                price=float(row['price'])
            )


#Этот код используется для импорта данных о ноутбуках из CSV-файла
# в базу данных Django, конкретно в модель Laptop приложения laptop_app.
