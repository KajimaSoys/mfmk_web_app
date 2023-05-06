# Generated by Django 4.1.2 on 2023-02-28 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_pricelist_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricelist',
            name='currency',
            field=models.CharField(choices=[('rub', 'руб.'), ('usd', '$'), ('eur', '€')], default='rub', max_length=30, verbose_name='Валюта'),
        ),
    ]