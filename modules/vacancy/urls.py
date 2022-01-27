from django.urls import path

from modules.vacancy.views import *

app_name = "vacancy"
urlpatterns = [
    path('vacancy/', VacancyList.as_view()),
    path('vacancy/<int:pk>', VacancySingle.as_view()),
]