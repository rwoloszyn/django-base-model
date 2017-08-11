from django.apps import AppConfig
from django.apps import apps
# https://stackoverflow.com/questions/6791911/execute-code-when-django-starts-once-only
from django_base_model.conf import conf


class BaseModelAppConfig(AppConfig):
    name = 'django-base-model'
    verbose_name = "Django base model"

    def ready(self):
        _validate_model_inheritance()


def _validate_model_inheritance():
    app = apps.get_app('my_application_name')

    for model in apps.get_models(include_auto_created=True):
        new_object = model()
        print(new_object)
        #
        # places = Place.objects.all()
        # not_restaurants = [p for p in places if not hasattr(p, 'restaurant')]


def _validate_custom_base_model():
    #checks whatever custom base model declared in settings is
    #abstract, so model instances are not created in db

    default_model = conf.DEFAULT_BASE_MODEL

    if not default_model._meta.abstract:
        raise Exception("DEFAULT_BASE_MODEL should be abstract class")
