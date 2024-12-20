# Generated by Django 5.0.6 on 2024-12-19 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laptop_app', '0003_alter_laptop_ram_alter_laptop_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='laptop',
            old_name='ram',
            new_name='internal_storage_gb',
        ),
        migrations.RemoveField(
            model_name='laptop',
            name='cpu',
        ),
        migrations.AddField(
            model_name='laptop',
            name='battery_life_h',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='laptop',
            name='ram_memory',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='laptop',
            name='weight_kg',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='brand',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='rating',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='year',
            field=models.IntegerField(null=True),
        ),
    ]
