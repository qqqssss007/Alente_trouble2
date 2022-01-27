import datetime

from django.db import models


class Conference(models.Model):
    title = models.CharField(
        null=False,
        blank=False,
        max_length=150,
    )
    text = models.TextField(
        null=False,
        blank=False,
    )
    creation_time = models.DateTimeField(
        default=datetime.datetime.now()
    )
    stert_time = models.DateTimeField()
    # todo: Добавить юзера
    # owner = models.ForeignKey(
    #     myUser,
    #     on_delete=models.CASCADE
    # )
