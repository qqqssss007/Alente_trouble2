from django.db import models

from modules.conference.models import Conference


class ConferenceResponce(models.Model):
    conference = models.ForeignKey(
        Conference,
        on_delete=models.CASCADE
    )
    # todo: Добавить юзера
    # owner = models.ForeignKey(
    #     myUser,
    #     on_delete=models.CASCADE
    # )
