from django.conf import settings

from django_base_model import models


class Settings(object):
    """
    Shadow Django's settings with a little logic
    """

    @property
    def BASE_MODEL_DEFAULT(self):
        return getattr(settings, 'BASE_MODEL_DEFAULT', models.BaseModel)


conf = Settings()
