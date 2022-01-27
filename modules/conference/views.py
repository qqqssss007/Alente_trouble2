import django_filters
from rest_framework import generics, filters
from rest_framework.permissions import AllowAny

from modules.conference.models import Conference
from modules.conference.serializers.conference import ConferenceSerializer


class ConferenceList(generics.ListCreateAPIView):
    queryset = Conference.objects.all()
    serializer_class = ConferenceSerializer
    permission_classes = [AllowAny]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = '__all__'
    search_fields = ['title']


class ConferenceSingle(generics.RetrieveAPIView, generics.DestroyAPIView, generics.UpdateAPIView):
    queryset = Conference.objects.all()
    serializer_class = ConferenceSerializer
    permission_classes = [AllowAny]
