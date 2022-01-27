from rest_framework import serializers
from modules.vacancy_responce.models import VacancyResponce


class VacancyResponceSerializer(serializers.ModelSerializer):
    class Meta:
        model = VacancyResponce
        fields = '__all__'