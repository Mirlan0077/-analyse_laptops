# Generated by Django 5.1.4 on 2024-12-17 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laptop_app', '0002_rename_manufacturer_laptop_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptop',
            name='ram',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='rating',
            field=models.FloatField(null=True),
        ),
    ]
