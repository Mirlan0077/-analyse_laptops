# Generated by Django 5.1.4 on 2024-12-17 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laptop_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='laptop',
            old_name='manufacturer',
            new_name='brand',
        ),
    ]
