from django.contrib import admin
from .models import *


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    model = Client

@admin.register(Questionnaire)
class QuestionnareAdmin(admin.ModelAdmin):
    model = Questionnaire
