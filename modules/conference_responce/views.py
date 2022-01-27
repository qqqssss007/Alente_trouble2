import django_filters
from rest_framework import generics, filters
from rest_framework.permissions import AllowAny

from modules.conference_responce.models import ConferenceResponce
from modules.conference_responce.serializers.conference_responce import ConferenceResponceSerializer


class ConferenceResponceList(generics.ListCreateAPIView):
    queryset = ConferenceResponce.objects.all()
    serializer_class = ConferenceResponceSerializer
    permission_classes = [AllowAny]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = '__all__'
    search_fields = ['title']


class ConferenceResponceSingle(generics.RetrieveAPIView, generics.DestroyAPIView, generics.UpdateAPIView):
    queryset = ConferenceResponce.objects.all()
    serializer_class = ConferenceResponceSerializer
    permission_classes = [AllowAny]
