from rest_framework import serializers
from modules.conference_responce.models import ConferenceResponce


class ConferenceResponceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConferenceResponce
        fields = '__all__'

