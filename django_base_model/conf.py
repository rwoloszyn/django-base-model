from django.conf import settings

from django_base_model import models


class Settings(object):
    """
    Shadow Django's settings with a little logic
    """

    @property
    def DEFAULT_BASE_MODEL(self):
        return getattr(settings, 'DEFAULT_BASE_MODEL', models.BaseModel)


conf = Settings()