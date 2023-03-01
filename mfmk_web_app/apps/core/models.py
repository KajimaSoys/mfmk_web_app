from django.db import models
import json, os
from django.contrib.postgres.fields import ArrayField
from mfmk_web_app.apps.core.utils import *
from mfmk_web_app.apps.core.waybill_engine import *
from multiselectfield import MultiSelectField
from itertools import groupby

class Client(models.Model):
    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


    id = models.BigAutoField(verbose_name="Идентификатор", primary_key=True)
    entity_name = models.CharField(verbose_name="Организация", max_length=200, blank=True)
    name = models.CharField(verbose_name="Фамилия, имя, отчество", max_length=200, blank=True)
    post = models.CharField(verbose_name="Должность", max_length=200, blank=True)
    email = models.CharField(verbose_name="Email", max_length=200, blank=True)
    number = models.CharField(verbose_name="Контактный телефон", max_length=200, blank=True)
    city = models.CharField(verbose_name="Город", max_length=200, blank=True)

    def __str__(self):
        return self.entity_name


class Questionnaire(models.Model):
    class Meta:
        verbose_name = 'Опросный лист'
        verbose_name_plural = 'Опросные листы'


    id = models.BigAutoField(verbose_name="Идентификатор", primary_key=True)

    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Дата изменения", auto_now=True)

    client = models.ForeignKey(to=Client, verbose_name="Клиент", on_delete=models.CASCADE, blank=True)

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
    sup_parameter = MultiSelectField(verbose_name="Поддерживаемый параметр", max_length=31, choices=sup_parameter_choices, blank=True)

    volume_pump = models.BooleanField(verbose_name="Насос", default=False)
    volume_pump_mark = models.CharField(verbose_name="Маркировка", max_length=100, blank=True)

    volume_fan = models.BooleanField(verbose_name="Вентилятор", default=False)
    volume_fan_mark = models.CharField(verbose_name="Маркировка", max_length=100, blank=True)

    volume_smoke_exhauster = models.BooleanField(verbose_name="Дымосос", default=False)
    volume_smoke_exhauster_mark = models.CharField(verbose_name="Маркировка", max_length=100, blank=True)

    volume_gate_valves = models.BooleanField(verbose_name="Задвижки", default=False)
    volume_gate_valves_mark = models.CharField(verbose_name="Маркировка", max_length=100, blank=True)

    def default_json():
        return [
            ['', '', '', '', '', '', ],
            ['', '', '', '', '', '', ],
            ['', '', '', '', '', '', ],
            ['', '', '', '', '', '', ],
        ]

    engine_data = models.JSONField(verbose_name="Данные электродвигателей", encoder=json.JSONEncoder , decoder=json.JSONDecoder, default=default_json, blank=True)

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
        ('one_freq', 'Один преобразователь частоты'),
        ('for_each', 'ПЧ на каждый электродвигатель'),
    )
    engine_control = models.CharField(verbose_name="Управление двигателями", max_length=50, choices=engine_control_choices, blank=True)

    # one_freq = models.BooleanField(verbose_name="Один преобразователь частоты", default=False)
    # for_each = models.BooleanField(verbose_name="ПЧ на каждый электродвигатель", default=False)

    power_inputs_choices = (
        ('two_power_ats', 'Два ввода питания (с АВР)'),
        ('two_power_noats', 'Два ввода питания (без АВР)'),
        ('one_power', 'Один ввод питания'),
    )
    power_inputs = models.CharField(verbose_name="Количество вводов питания", max_length=30, choices=power_inputs_choices, blank=True)

    add_information = models.TextField(verbose_name="Дополнительные сведения", blank=True)

    main_data = models.TextField(verbose_name="Название и расположение объекта", blank=True)

    source_choices = (
        ('ad', 'Реклама Яндекс / Google'),
        ('search', 'Поиск Яндекс / Google'),
        ('social', 'Социальные сети'),
        ('friends', 'Рекомендации коллег, друзей'),
        ('work', 'Уже знали о нас, работали с нами'),
    )
    source = models.CharField(verbose_name="Как узнали", max_length=50, choices=source_choices, blank=True)
    source_another = models.TextField(verbose_name="Другое", blank=True)

    path = models.CharField(verbose_name="Путь до файла", max_length=50, blank=True)

    def __str__(self):
        return f'{self.id}' + f' - {self.main_data}' if self.main_data != '' else ''


    def get_name(self):
        return f'{self.id}' + f' - {self.client.entity_name}' #if self.main_data != '' else ''


    def get_size(self):
        if self.cabinet_width and self.cabinet_height and self.cabinet_depth:
            return f'{self.cabinet_width}x{self.cabinet_height}x{self.cabinet_depth}'
        else:
            return 'Отсутствуют'


    def sup_parameter_translate(self):
        return str(self.sup_parameter)


    def update_model(self):
        """Создание директории клиента при сохранении"""
        path = f'id_{self.id}'
        try:
            os.mkdir(f'media/questionnaire/{path}')
            print(f'media/questionnaire/{path}')
            print(f"Directory media/questionnaire/{path} created!")
        except FileExistsError:
            print(f"Directory media/questionnaire/{path} already exists")

        Questionnaire.objects.filter(id=self.id).update(path=f'media/questionnaire/{path}')
        # client = Client.objects.get(id=self.client_id)

        if generate_pdf(self, self.client):
            print('Pdf file generated successfully!')
        else:
            print('An error occurred while generating the pdf document :(')

        price_positions = self.handle_data()

        if generate_waybill(self, price_positions):
            print('Waybill file generated successfully!')
        else:
            print('An error occurred while generating the waybill document :(')


    def save(self, *args, **kwargs):
        super(Questionnaire, self).save(*args, **kwargs)
        self.update_model()

    def handle_data(self):
        positions = PriceList.objects.filter(type__in=['tires', 'signalfittings', 'relays', 'consumables',])
        positions_by_type = {}
        if (self.system == 'firefighting') & (self.manufacturer == 'dek'):
            if 'level' in self.sup_parameter:
                if self.volume_pump:
                    if (self.engine_data[0][0] == '30') & (self.engine_data[0][1] == '30') & (self.engine_data[0][2] == '0,75'):
                        if self.cabinet_parameters == 'uhl4':
                            if (self.cabinet_width == '1000') & (self.cabinet_height == '600') & (self.cabinet_depth == '300'):
                                if (self.engine_control == 'smooth') & (self.power_inputs == 'two_power_ats'):
                                    vendors_code = [
                                        'MC1006030',
                                        '17011DEK',
                                        '21241DEK',
                                        '21280DEK',
                                        '21226DEK',
                                        '21271DEK',
                                        '22001DEK',
                                        '24105DEK',
                                        'ESQ-GS7-030',
                                        'MDR-60-24',
                                        'EDS-205A',
                                        '270130',
                                        '22008DEK',
                                        '24105DEK',
                                        '24118DEK',
                                        'MFK10',
                                        '820218',
                                        '820271',
                                        'PBO-AD33',
                                        '12301DEK'
                                    ]

                                    names_without_vendor = [
                                        'ОПЛК Vision V570 (3xAI, 18xDI, 17xDO)',
                                        'FLC'
                                    ]

                                    positions = positions\
                                        .union(PriceList.objects.filter(vendor_code__in=vendors_code))\
                                        .union(PriceList.objects.filter(name__in=names_without_vendor))

        positions = positions.order_by('type',)
        for key, group in groupby(positions, lambda x: x.type):
            positions_by_type[key] = list(group)

        return positions_by_type




class PriceList(models.Model):
    class Meta:
        verbose_name = "Позиция"
        verbose_name_plural = "Прайс-лист"
        ordering = ('type',)

    id = models.BigAutoField(verbose_name="Идентификатор", primary_key=True)

    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Дата изменения", auto_now=True)

    type_choices = (
        ('closet', 'Шкаф'),
        ('switching', 'Коммутационное оборудование'),
        ('softstarter', 'Пч и упп'),
        ('controllers', 'Контроллеры'),
        ('avr', 'Авр'),
        ('tires', 'Шины'),
        ('signalfittings', 'Сигнальная арматура и переключатели'),
        ('relays', 'Клеммы и реле'),
        ('consumables', 'Расходные материалы'),
    )

    type = models.CharField(verbose_name="Тип", choices=type_choices, max_length=30)
    name = models.CharField(verbose_name="Название", max_length=300, blank=True)
    vendor_code = models.CharField(verbose_name="Артикул", max_length=100, blank=True)
    manufacturer = models.CharField(verbose_name="Производитель", max_length=100, blank=True)
    price = models.FloatField(verbose_name="Цена без НДС", blank=True)

    currency_choices = (
        ('rub', 'руб.'),
        ('usd', '$'),
        ('eur', '€'),
    )

    currency = models.CharField(verbose_name="Валюта", choices=currency_choices, max_length=30, default='rub')

    def __str__(self):
        return self.name

    def get_price(self):
        return f'{self.price}{self.get_currency_display()}'

    get_price.short_description = "Цена без НДС"