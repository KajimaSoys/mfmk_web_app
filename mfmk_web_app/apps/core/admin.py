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

@admin.register(Questionnaire)
class QuestionnareAdmin(admin.ModelAdmin):
    model = Questionnaire

    Questionnaire.get_size.short_description = 'Размер шкафа (ШxВxГ)'

    list_display = ('id',
                  'system',
                  'manufacturer',
                  'sup_parameter',
                  'cabinet_parameters',
                  'get_size',
                  'one_freq',
                  'for_each',
                  # 'power_inputs',
                  'add_information',
                  'account_actions',
                  'created_at',)

    exclude = ('path',)

    def get_urls(self):
        urls = super(QuestionnareAdmin, self).get_urls()
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
            '<a class="button" href="{}">Скачать</a>',
            reverse('admin:generate_pdf', args=[obj.pk]),
        )

    account_actions.short_description = 'Опросный лист'
    account_actions.allow_tags = True

    def generate_pdf(self, request, id, *args, **kwargs):
        # data = data_format.get_data(uuid)
        # path = waybill_engine.waybill_generate(data)
        path = f'{Questionnaire.objects.get(id=id).path}/questionnare_{id}.pdf'
        # file_path =  path #settings.FILE_PATH_FIELD_DIRECTORY +
        # temp = slugify(path.split('/')[3][:-4])
        #
        print(path)
        if os.path.exists(path):
            with open(path, 'rb') as pdf:
                response = HttpResponse(pdf.read(), content_type='application/pdf')
                response['Content-Disposition'] = 'attachment; filename=questionnare_' + id + '.pdf'
                return response
                pdf.closed