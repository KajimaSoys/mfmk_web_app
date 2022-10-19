# Generated by Django 4.1.2 on 2022-10-18 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_questionnaire_system'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnaire',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата изменения'),
        ),
    ]