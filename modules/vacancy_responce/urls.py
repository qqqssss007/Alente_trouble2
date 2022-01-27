from django.urls import path

from modules.vacancy_responce.views import *

app_name = 'vacancy_responce'
urlpatterns = [
    path('/', VacancyResponceList.as_view()),
    path('vacancy/<int:pk>', VacancyResponceSingle.as_view()),
]