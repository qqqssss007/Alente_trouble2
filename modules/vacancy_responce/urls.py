from django.urls import path

from modules.vacancy_responce.views import *

app_name = 'vacancy_responce'
urlpatterns = [
    path('vacancy_responce/', VacancyResponceList.as_view()),
    path('vacancy_responce/<int:pk>', VacancyResponceSingle.as_view()),
]