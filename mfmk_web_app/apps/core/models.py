from django.db import models
from django.contrib.postgres.fields import ArrayField

class Client(models.Model):
    id = models.BigAutoField(verbose_name="Идентификатор", primary_key=True)
    entity_name = models.CharField(verbose_name="Организация", max_length=200)
    name = models.CharField(verbose_name="Фамилия, имя, отчество", max_length=200)
    post = models.CharField(verbose_name="Должность", max_length=200)
    email = models.CharField(verbose_name="Email", max_length=200)
    number = models.CharField(verbose_name="Контактный телефон", max_length=200)
    city = models.CharField(verbose_name="Город", max_length=200)


class Questionnaire(models.Model):
    id = models.BigAutoField(verbose_name="Идентификатор", primary_key=True)

    system_choices = (
        ('heating', 'Отопление'),
        ('water_supply', 'Водоснабжение'),
        ('pumping_station', 'КНС'),
        ('firefighting', 'Пожаротушение'),
    )
    system = models.CharField(verbose_name="Система", max_length=30, choices=system_choices)

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

    # volume_choices = (
    #     ('pump', 'Насос'),
    #     ('fan', 'Вентилятор'),
    #     ('smoke_exhauster', 'Дымосос'),
    #     ('gate_valves', 'Задвижки'),
    # )
    # volume = models.CharField(verbose_name="Объем теплоносителя в системе (литр)", max_length=30, choices=volume_choices, blank=True)

    # volume_mark = models.CharField(verbose_name="Маркировка", max_length=50, blank=True)

    # engine_data = ArrayField(
    #     ArrayField(
    #         models.CharField(max_length=10),
    #         size=4, blank=True),
    #     size=6, blank=True)

    cabinet_parameters_choices = (
        ('uhl4', 'УХЛ4'),
        ('uhl2', 'УХЛ2'),
        ('uhl1', 'УХЛ1'),
    )
    cabinet_parameters = models.CharField(verbose_name="Параметры шкафа и окружающей среды", max_length=15, choices=cabinet_parameters_choices, blank=True)

    engine_control_choices = (
        ('direct', 'Прямой пуск'),
        ('smooth', 'Плавный пуск'),
        ('frequency', 'Частотное регулирование'),
        ('one_freq', 'Один преобразователь частоты'),
        ('for_each', 'ПЧ на каждый электродвигатель'),
    )
    engine_control = models.CharField(verbose_name="Управление двигателями", max_length=30, choices=engine_control_choices, blank=True)
    #TODO последние два вынести в отдельное поле

    power_inputs_choices = (
        ('two_power_ats', 'Два ввода питания (с АВР)'),
        ('two_power_noats', 'Два ввода питания (без АВР)'),
        ('one_power', 'Один ввод питания'),
    )
    power_inputs = models.CharField(verbose_name="Количество вводов питания", max_length=30, choices=power_inputs_choices, blank=True)

    add_information = models.TextField(verbose_name="Дополнительные сведения ", blank=True)