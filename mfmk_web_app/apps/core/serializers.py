from django.contrib.auth.models import User, Group
from mfmk_web_app.apps.core.models import Questionnaire
from rest_framework import serializers, fields

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class QuestionnaireSerializer(serializers.HyperlinkedModelSerializer):
    sup_parameter = serializers.MultipleChoiceField(choices=Questionnaire.sup_parameter_choices)
    class Meta:
        model = Questionnaire
        fields = ['id',
                  'system',
                  'manufacturer',
                  'sup_parameter',
                  'volume_pump',
                  'volume_pump_mark',
                  'volume_fan',
                  'volume_fan_mark',
                  'volume_smoke_exhauster',
                  'volume_smoke_exhauster_mark',
                  'volume_gate_valves',
                  'volume_gate_valves_mark',
                  'engine_data',
                  'cabinet_parameters',
                  'cabinet_width',
                  'cabinet_height',
                  'cabinet_depth',
                  'engine_control',
                  'power_inputs',
                  'add_information',
                  'path',]
