from django.contrib import admin
from django.contrib.admin.forms import AdminPasswordChangeForm

from users.models import User
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email', 'is_active', ]
    fields = ('username', 'password', 'first_name', 'last_name', 'email', 'is_active', 'birthday', 'groups')
    change_password_form = AdminPasswordChangeForm

