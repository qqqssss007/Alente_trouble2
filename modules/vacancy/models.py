from django.db import models


class Vacancy(models.Model):
    title = models.CharField(
        null=False,
        blank=False,
        max_length=150,
    )
    text = models.TextField(
        null=False,
        blank=False,
    )
    contact_email = models.EmailField()