from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.urls import re_path as url
from .models import *
from mfmk_web_app import settings
from django.http import HttpResponse


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    model = Client

    list_display = (
        'entity_name',
        'name',
        'post',
        'email',
        'number',
        'city',
        'orders',
    )

    search_fields = ('entity_name', 'name', 'id')

    def orders(self, obj):
        html = ''
        questionnaire = Questionnaire.objects.filter(client_id=obj.pk)
        for item in questionnaire:
            id = item.id
            main_data = item.main_data
            template = f'<a class="btn btn-outline-primary" href="../questionnaire/{id}">№{id} - {main_data}</a><p></p>'
            html = html + template
        return format_html(html[:-7])

    orders.short_description = 'Заказы'
    orders.allow_tags = True



@admin.register(Questionnaire)
class QuestionnaireAdmin(admin.ModelAdmin):
    model = Questionnaire


    Questionnaire.get_size.short_description = 'Размер шкафа (ШxВxГ)'
    Questionnaire.sup_parameter_translate.short_description = "Поддерживаемый параметр"
    Questionnaire.get_name.short_description = "Название"

    list_display = (
        'get_name',
        'system',
        'manufacturer',
        'sup_parameter_translate',
        'cabinet_parameters',
        'get_size',
        'engine_control',
        # 'one_freq',
        # 'for_each',
        # 'power_inputs',
        'add_information',
        'account_actions',
        'created_at',
    )

    exclude = ('path',)

    search_fields = ('client__entity_name', 'client__name', 'id')

    def get_urls(self):
        urls = super(QuestionnaireAdmin, self).get_urls()
        custom_urls = [
            url(
                r'^(?P<id>.+)/generate_pdf/$',
                self.admin_site.admin_view(self.generate_pdf),
                name='generate_pdf',
            ),
        ]
        return custom_urls + urls

    def account_actions(self, obj):
        return format_html(
            '<a class="btn btn-outline-primary" href="{}">Скачать</a>',
            reverse('admin:generate_pdf', args=[obj.pk]),
        )

    account_actions.short_description = 'Опросный лист'
    account_actions.allow_tags = True

    def generate_pdf(self, request, id, *args, **kwargs):
        path = f'{Questionnaire.objects.get(id=id).path}/questionnaire_{id}.pdf'
        if os.path.exists(path):
            with open(path, 'rb') as pdf:
                response = HttpResponse(pdf.read(), content_type='application/pdf')
                response['Content-Disposition'] = 'attachment; filename=questionnaire_' + id + '.pdf'
                return response
                pdf.closed

