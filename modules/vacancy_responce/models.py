from django.db import models

from modules.vacancy.models import Vacancy


class VacancyResponce(models.Model):
    vacancy = models.ForeignKey(
        Vacancy,
        on_delete=models.CASCADE
    )
    # todo: Добавить юзера
    # owner = models.ForeignKey(
    #     myUser,
    #     on_delete=models.CASCADE
    # )
    resume_file = models.FileField()
