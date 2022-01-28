from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from modules.Users import views

app_name = "Users"
urlpatterns = [
    path('registration', views.registration, name='registration'),
    path('authorization', views.authorization, name='authorization'),
]
