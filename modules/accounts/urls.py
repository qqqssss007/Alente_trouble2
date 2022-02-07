from django.urls import path

from modules.accounts.views import *

app_name = 'accounts'
urlpatterns = [
    path('accounts/', AccountsList.as_view()),
    path('accounts/<int:pk>', AccountsSingle.as_view()),
]