# Generated by Django 5.0.10 on 2024-12-20 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laptop_app', '0007_laptop_brand_laptop_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='laptop',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='laptop',
            name='model',
        ),
    ]