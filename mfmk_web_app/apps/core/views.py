from django.shortcuts import render
from django.contrib.auth.models import User, Group
from mfmk_web_app.apps.core.models import Questionnaire
from rest_framework import viewsets
from rest_framework import permissions
from mfmk_web_app.apps.core.serializers import UserSerializer, GroupSerializer, QuestionnareSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class QuestionnareViewSet(viewsets.ModelViewSet):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnareSerializer
    permission_classes = []
    authentication_classes = []
