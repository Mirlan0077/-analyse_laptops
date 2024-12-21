import pandas as pd
from django.db import transaction
from django.db.models.signals import pre_save
from laptop_app.models import Laptop, calculate_rating

def process_csv(file_path):

    data = pd.read_csv(file_path)
    data = data.rename(columns={
        'Name': 'name',
        'PriceEUR': 'price_eur',
        'DisplayInch': 'display_inch',
        'DisplayCM': 'display_cm',
        'DisplayResolution': 'display_resolution',
        'DisplayRatio': 'display_ratio',
        'WeightKG': 'weight_kg',
        'HeightMM': 'height_mm',
        'WidthMM': 'width_mm',
        'DepthMM': 'depth_mm',
        'OperatingSystem': 'operating_system',
        'CPUProcessor': 'cpu_processor',
        'RAMMemory': 'ram_memory',
        'GPUIntegrated': 'gpu_integrated',
        'GPUExtra': 'gpu_extra',
        'InternalStorageGB': 'internal_storage_gb',
        'StorageType': 'storage_type',
        'BatteryLifeH': 'battery_life_h',
        'BatteryCapacityWH': 'battery_capacity_wh',
        'PSUWatts': 'psu_watts',
        'AudioSystem': 'audio_system',
        'SpeakersCount': 'speakers_count',
        'HasTouchscreen': 'has_touchscreen',
        'KeyboardBacklit': 'keyboard_backlit',
        'KeyboardNumpad': 'keyboard_numpad',
        'HasWebcam': 'has_webcam',
        'HasBluetooth': 'has_bluetooth',
        'BluetoothVersion': 'bluetooth_version',
        'WiFiStandard': 'wifi_standard',
        'ProductEAN': 'product_ean',
        'ProductSKU': 'product_sku',
        'ReleaseYear': 'release_year',
        'Category': 'category'
    })

    data['battery_life_h'] = data['battery_life_h'].fillna(0)
    data['weight_kg'] = data['weight_kg'].replace(0, 1.0)
    data['ram_memory'] = data['ram_memory'].fillna(0)
    data['internal_storage_gb'] = data['internal_storage_gb'].fillna(0)

    data['display_inch'] = data['display_inch'].fillna(0)
    data['display_cm'] = data['display_cm'].fillna(0)
    data['display_resolution'] = data['display_resolution'].fillna('Unknown')
    data['display_ratio'] = data['display_ratio'].fillna('Unknown')
    data['height_mm'] = data['height_mm'].fillna(0)
    data['width_mm'] = data['width_mm'].fillna(0)
    data['depth_mm'] = data['depth_mm'].fillna(0)
    data['operating_system'] = data['operating_system'].fillna('Unknown')
    data['cpu_processor'] = data['cpu_processor'].fillna('Unknown')
    data['gpu_extra'] = data['gpu_extra'].fillna('None')
    data['storage_type'] = data['storage_type'].fillna('Unknown')
    data['battery_capacity_wh'] = data['battery_capacity_wh'].fillna(0)
    data['psu_watts'] = data['psu_watts'].fillna(0)
    data['audio_system'] = data['audio_system'].fillna('Unknown')
    data['speakers_count'] = data['speakers_count'].fillna(0)
    data['bluetooth_version'] = data['bluetooth_version'].fillna(0)
    data['wifi_standard'] = data['wifi_standard'].fillna('Unknown')
    data['product_ean'] = data['product_ean'].fillna('Unknown')
    data['product_sku'] = data['product_sku'].fillna('Unknown')
    data['release_year'] = data['release_year'].fillna(0)
    data['category'] = data['category'].fillna('Unknown')

    # Итерация по строкам и сохранение каждого ноутбука в базу
    with transaction.atomic():
        pre_save.disconnect(calculate_rating, sender=Laptop)
        for _, row in data.iterrows():
            laptop, created = Laptop.objects.update_or_create(
                product_sku=row['product_sku'],
                defaults={
                'name': row['name'],
                'price_eur': row['price_eur'],
                'display_inch':row['display_inch'],
                'display_cm':row['display_cm'],
                'display_resolution':row['display_resolution'],
                'display_ratio':row['display_ratio'],
                'weight_kg':row['weight_kg'],
                'height_mm':row['height_mm'],
                'width_mm':row['width_mm'],
                'depth_mm':row['depth_mm'],
                'operating_system':row['operating_system'],
                'cpu_processor':row['cpu_processor'],
                'ram_memory':row['ram_memory'],
                'gpu_integrated':row['gpu_integrated'] == 'True',
                'gpu_extra':row['gpu_extra'],
                'internal_storage_gb':row['internal_storage_gb'],
                'storage_type':row['storage_type'],
                'battery_life_h':row['battery_life_h'],
                'battery_capacity_wh':row['battery_capacity_wh'],
                'psu_watts':row['psu_watts'],
                'audio_system':row['audio_system'],
                'speakers_count':row['speakers_count'],
                'has_touchscreen':row['has_touchscreen'] == 'True',
                'keyboard_backlit':row['keyboard_backlit'] == 'True',
                'keyboard_numpad':row['keyboard_numpad'] == 'True',
                'has_webcam':row['has_webcam'] == 'True',
                'has_bluetooth':row['has_bluetooth'] == 'True',
                'bluetooth_version':row['bluetooth_version'],
                'wifi_standard':row['wifi_standard'],
                'product_ean':row['product_ean'],
                'product_sku':row['product_sku'],
                'release_year':row['release_year'],
                'category':row['category']
            }
            )

            laptop.rating = laptop.calculate_score()
            laptop.save()
