import reversion
from django.db import models

from django.contrib.auth.models import AbstractUser


@reversion.register()
class User(AbstractUser):
    first_name = models.CharField(
        verbose_name='Имя',
        null=False,
        blank=False,
        max_length=50
    )
    email = models.EmailField(
        verbose_name='Почта',
        null=False,
        blank=False,
        max_length=50
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.email}'
