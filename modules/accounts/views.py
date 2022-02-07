import django_filters
from rest_framework import generics, filters
from rest_framework.permissions import AllowAny

from modules.accounts.models import MyUser
from modules.accounts.serializers.accounts import MyUserSerializer


class AccountsList(generics.ListCreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
    permission_classes = [AllowAny]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = '__all__'
    search_fields = ['phone_number']


class AccountsSingle(generics.RetrieveAPIView, generics.DestroyAPIView, generics.UpdateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
    permission_classes = [AllowAny]

