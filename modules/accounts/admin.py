from django.contrib import admin

from modules.accounts.models import MyUser

admin.site.register(MyUser)
