from django.db import models
from django.utils import timezone


class CustomAbstractBaseModel(models.Model):
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class CustomNonAbstractBaseModel(models.Model):
    is_active = models.BooleanField(default=True)

