from django.db import models
from authemail.models import EmailUserManager, EmailAbstractUser


class MyUser(EmailAbstractUser):
    phone_number = models.IntegerField('Phone number', null=True, blank=True)
    date_of_birth = models.DateField('Date of birth', null=True, blank=True)

    objects = EmailUserManager()

