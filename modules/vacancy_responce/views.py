import django_filters
from rest_framework import generics, filters
from rest_framework.permissions import AllowAny

from modules.vacancy_responce.models import VacancyResponce
from modules.vacancy_responce.serializers.vacancy_responce import VacancyResponceSerializer


class VacancyResponceList(generics.ListCreateAPIView):
    queryset = VacancyResponce.objects.all()
    serializer_class = VacancyResponceSerializer
    permission_classes = [AllowAny]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = '__all__'
    search_fields = ['title']


class VacancyResponceSingle(generics.RetrieveAPIView, generics.DestroyAPIView, generics.UpdateAPIView):
    queryset = VacancyResponce.objects.all()
    serializer_class = VacancyResponceSerializer
    permission_classes = [AllowAny]
