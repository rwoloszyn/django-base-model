from django.apps import AppConfig
from django.apps import apps
# https://stackoverflow.com/questions/6791911/execute-code-when-django-starts-once-only
from django.core.exceptions import ImproperlyConfigured


class BaseModelAppConfig(AppConfig):
    name = 'django_base_model'
    verbose_name = "Django base model"

    def ready(self):
        pass
        # _validate_model_inheritance()


def _validate_model_inheritance():
    # app = apps.get_app('my_application_name')

    for model in apps.get_models():
        new_object = model()
        if new_object._meta.abstract is False:
            raise ImproperlyConfigured("BASE_MODEL_DEFAULT should be an abstract class")
        #
        # places = Place.objects.all()
        # not_restaurants = [p for p in places if not hasattr(p, 'restaurant')]


def _validate_base_model():
    # checks whatever custom base model declared in settings is
    # abstract, so model instances are not created in db
    from django_base_model.conf import conf

    default_model = conf.BASE_MODEL_DEFAULT

    if default_model._meta.abstract is False:
        raise ImproperlyConfigured("BASE_MODEL_DEFAULT should be an abstract class")
