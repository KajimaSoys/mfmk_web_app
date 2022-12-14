# Generated by Django 4.1.2 on 2022-10-26 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_remove_questionnaire_for_each_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnaire',
            name='client',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='core.client', verbose_name='Клиент'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='main_data',
            field=models.TextField(blank=True, verbose_name='Название и расположение объекта'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='source',
            field=models.CharField(blank=True, choices=[('ad', 'Реклама Яндекс / Google'), ('search', 'Поиск Яндекс / Google'), ('social', 'Социальные сети'), ('friends', 'Рекомендации коллег, друзей'), ('work', 'Уже знали о нас, работали с нами')], max_length=50, verbose_name='Как узнали'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='source_another',
            field=models.TextField(blank=True, verbose_name='Другое'),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='add_information',
            field=models.TextField(blank=True, verbose_name='Дополнительные сведения'),
        ),
    ]
