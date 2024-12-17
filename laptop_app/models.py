from django.db import models


class Laptop(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    year = models.IntegerField()
    rating = models.FloatField(null=True)
    cpu = models.CharField(max_length=255)
    ram = models.IntegerField(null=True)
    price = models.FloatField()

    def __str__(self):
        return f"{self.name} ({self.brand})"