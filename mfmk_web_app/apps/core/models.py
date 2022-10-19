from django.db import models
import json, os
from django.contrib.postgres.fields import ArrayField
from mfmk_web_app.apps.core.utils import *

class Client(models.Model):
    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


    id = models.BigAutoField(verbose_name="Идентификатор", primary_key=True)
    entity_name = models.CharField(verbose_name="Организация", max_length=200)
    name = models.CharField(verbose_name="Фамилия, имя, отчество", max_length=200)
    post = models.CharField(verbose_name="Должность", max_length=200)
    email = models.CharField(verbose_name="Email", max_length=200)
    number = models.CharField(verbose_name="Контактный телефон", max_length=200)
    city = models.CharField(verbose_name="Город", max_length=200)


class Questionnaire(models.Model):
    class Meta:
        verbose_name = 'Опросный лист'
        verbose_name_plural = 'Опросные листы'


    id = models.BigAutoField(verbose_name="Идентификатор", primary_key=True)

    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Дата изменения", auto_now=True)

    system_choices = (
        ('heating', 'Отопление'),
        ('water_supply', 'Водоснабжение'),
        ('pumping_station', 'КНС'),
        ('firefighting', 'Пожаротушение'),
    )
    system = models.CharField(verbose_name="Система", max_length=30, choices=system_choices, blank=True)

    manufacturer_choices = (
        ('dek', 'DEK'),
        ('iek', 'IEK'),
        ('ekf', 'EKF'),
        ('keaz', 'КЭАЗ'),
    )

    manufacturer = models.CharField(verbose_name="Производитель", max_length=10, choices=manufacturer_choices, blank=True)

    sup_parameter_choices = (
        ('pressure', 'Давление'),
        ('temperature', 'Температура'),
        ('flow', 'Расход'),
        ('level', 'Уровень'),
    )
    sup_parameter = models.CharField(verbose_name="Поддерживаемый параметр", max_length=30, choices=sup_parameter_choices, blank=True)

    volume_pump = models.BooleanField(verbose_name="Насос", default=False)
    volume_pump_mark = models.CharField(verbose_name="Маркировка", max_length=100, blank=True)

    volume_fan = models.BooleanField(verbose_name="Вентилятор", default=False)
    volume_fan_mark = models.CharField(verbose_name="Маркировка", max_length=100, blank=True)

    volume_smoke_exhauster = models.BooleanField(verbose_name="Дымосос", default=False)
    volume_smoke_exhauster_mark = models.CharField(verbose_name="Маркировка", max_length=100, blank=True)

    volume_gate_valves = models.BooleanField(verbose_name="Задвижки", default=False)
    volume_gate_valves_mark = models.CharField(verbose_name="Маркировка", max_length=100, blank=True)

    engine_data = models.JSONField(verbose_name="Данные электродвигателей", encoder=json.JSONEncoder , decoder=json.JSONDecoder, blank=True)

    cabinet_parameters_choices = (
        ('uhl4', 'УХЛ4'),
        ('uhl2', 'УХЛ2'),
        ('uhl1', 'УХЛ1'),
    )
    cabinet_parameters = models.CharField(verbose_name="Параметры шкафа и окружающей среды", max_length=15, choices=cabinet_parameters_choices, blank=True)
    cabinet_width = models.CharField(verbose_name="Ширина шкафа, мм", max_length=10, blank=True)
    cabinet_height = models.CharField(verbose_name="Высота шкафа, мм", max_length=10, blank=True)
    cabinet_depth = models.CharField(verbose_name="Глубина шкафа, мм", max_length=10, blank=True)


    engine_control_choices = (
        ('direct', 'Прямой пуск'),
        ('smooth', 'Плавный пуск'),
        ('frequency', 'Частотное регулирование'),
        # ('one_freq', 'Один преобразователь частоты'),
        # ('for_each', 'ПЧ на каждый электродвигатель'),
    )
    engine_control = models.CharField(verbose_name="Управление двигателями", max_length=30, choices=engine_control_choices, blank=True)

    one_freq = models.BooleanField(verbose_name="Один преобразователь частоты", default=False)
    for_each = models.BooleanField(verbose_name="ПЧ на каждый электродвигатель", default=False)

    power_inputs_choices = (
        ('two_power_ats', 'Два ввода питания (с АВР)'),
        ('two_power_noats', 'Два ввода питания (без АВР)'),
        ('one_power', 'Один ввод питания'),
    )
    power_inputs = models.CharField(verbose_name="Количество вводов питания", max_length=30, choices=power_inputs_choices, blank=True)

    add_information = models.TextField(verbose_name="Дополнительные сведения ", blank=True)

    path = models.CharField(verbose_name="Путь до файла", max_length=50, blank=True)

    def get_size(self):
        if self.cabinet_width and self.cabinet_height and self.cabinet_depth:
            return f'{self.cabinet_width}x{self.cabinet_height}x{self.cabinet_depth}'
        else:
            return 'Отсутствуют'


    def update_model(self):
        """Создание директории клиента при сохранении"""
        path = f'id_{self.id}'
        try:
            os.mkdir(f'media/questionnare_pdf/{path}')
            print("Directory media/questionnare_pdf/", path, " created!")
        except FileExistsError:
            print("Directory media/questionnare_pdf/", path, " already exists")

        Questionnaire.objects.filter(id=self.id).update(path=f'media/questionnare_pdf/{path}')



    def save(self, *args, **kwargs):
        super(Questionnaire, self).save(*args, **kwargs)
        self.update_model()

        if generate_pdf(self):
            print('Pdf file generated successfully!')
        else:
            print('An error occurred while generating the pdf document :(')