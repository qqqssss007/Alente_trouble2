from django.urls import path

from modules.conference_responce.views import *

app_name = "conference_responce"
urlpatterns = [
    path('conference_responce/', ConferenceResponceList.as_view()),
    path('conference_responce/<int:pk>', ConferenceResponceSingle.as_view()),
]
