from django.urls import path

from modules.conference.views import *

app_name = "conference"
urlpatterns = [
    path('conference/', ConferenceList.as_view()),
    path('conference/<int:pk>', ConferenceSingle.as_view()),
]
