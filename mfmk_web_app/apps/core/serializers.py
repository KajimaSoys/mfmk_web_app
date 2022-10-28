from django.contrib.auth.models import User, Group
from mfmk_web_app.apps.core.models import Questionnaire, Client
from rest_framework import serializers, fields

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = [
            'id',
            'entity_name',
            'name',
            'post',
            'email',
            'number',
            'city',
        ]

class QuestionnaireSerializer(serializers.HyperlinkedModelSerializer):
    client = ClientSerializer()
    sup_parameter = serializers.MultipleChoiceField(choices=Questionnaire.sup_parameter_choices)
    class Meta:
        model = Questionnaire
        fields = ['id',
                  'client',
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
                  'main_data',
                  'source',
                  'source_another',
                  'path',]

    def create(self, validated_data):
        client_data = validated_data.pop('client')
        client = Client.objects.create(**client_data)
        questionnaire = Questionnaire.objects.create(client=client, **validated_data)
        return questionnaire