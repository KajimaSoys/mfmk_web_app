from django.shortcuts import render
from django.contrib.auth.models import User, Group
from mfmk_web_app.apps.core.models import Questionnaire
from rest_framework import viewsets
from rest_framework import permissions
from mfmk_web_app.apps.core.serializers import UserSerializer, GroupSerializer, QuestionnaireSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class QuestionnaireViewSet(viewsets.ModelViewSet):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer
    permission_classes = []
    authentication_classes = []