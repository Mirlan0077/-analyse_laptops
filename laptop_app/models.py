from django.db import models


class Laptop(models.Model):
    name = models.CharField(max_length=255)
    price_eur = models.FloatField(null=True, blank=True)
    display_inch = models.FloatField(null=True, blank=True)
    display_cm = models.FloatField(null=True, blank=True)
    display_resolution = models.CharField(max_length=50, null=True, blank=True)
    display_ratio = models.CharField(max_length=20, null=True, blank=True)
    weight_kg = models.FloatField(null=True, blank=True)
    height_mm = models.FloatField(null=True, blank=True)
    width_mm = models.FloatField(null=True, blank=True)
    depth_mm = models.FloatField(null=True, blank=True)
    operating_system = models.CharField(max_length=50, null=True, blank=True)
    cpu_processor = models.CharField(max_length=100, null=True, blank=True)
    ram_memory = models.IntegerField(null=True, blank=True)
    gpu_integrated = models.BooleanField(default=False)
    gpu_extra = models.CharField(max_length=100, null=True, blank=True)
    internal_storage_gb = models.IntegerField(null=True, blank=True)
    storage_type = models.CharField(max_length=50, null=True, blank=True)
    battery_life_h = models.FloatField(null=True, blank=True)
    battery_capacity_wh = models.FloatField(null=True, blank=True)
    psu_watts = models.IntegerField(null=True, blank=True)
    audio_system = models.CharField(max_length=100, null=True, blank=True)
    speakers_count = models.IntegerField(null=True, blank=True)
    has_touchscreen = models.BooleanField(default=False)
    keyboard_backlit = models.BooleanField(default=False)
    keyboard_numpad = models.BooleanField(default=False)
    has_webcam = models.BooleanField(default=True)
    has_bluetooth = models.BooleanField(default=True)
    bluetooth_version = models.CharField(max_length=100, blank=True, null=True)
    wifi_standard = models.CharField(max_length=50, null=True, blank=True)
    product_ean = models.CharField(max_length=50, null=True, blank=True)
    product_sku = models.CharField(max_length=50, null=True, blank=True)
    release_year = models.IntegerField(null=True, blank=True)
    category = models.CharField(max_length=50, null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)

    def calculate_score(self):
        """Вычисляет рейтинг ноутбука."""
        try:
            ram_factor = (self.ram_memory / self.price_eur) * 0.4 if self.price_eur else 0
            storage_factor = (self.internal_storage_gb / self.price_eur) * 0.3 if self.price_eur else 0
            weight_factor = (1 / self.weight_kg) * 0.2 if self.weight_kg and self.weight_kg > 0 else 0
            battery_factor = (self.battery_life_h / 24) * 0.1 if self.battery_life_h else 0
            return ram_factor + storage_factor + weight_factor + battery_factor
        except ZeroDivisionError:
            return 0

    def save(self, *args, **kwargs):
        """Автоматически обновляет рейтинг перед сохранением."""
        self.rating = self.calculate_score()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.cpu_processor})"
