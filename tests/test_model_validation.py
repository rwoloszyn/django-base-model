from django.core.exceptions import ImproperlyConfigured
from django.test import SimpleTestCase
from django.test import override_settings

from django_base_model.apps import _validate_base_model, _validate_model_inheritance
from tests.test_app.models import CustomAbstractBaseModel, CustomNonAbstractBaseModel


class ModelValidTests(SimpleTestCase):
    def test_is_default_base_model_abstract(self):
        self.assertRaisesMessage(ImproperlyConfigured, _validate_base_model)

    @override_settings(BASE_MODEL_DEFAULT=CustomAbstractBaseModel)
    def test_is_custom_base_model_abstract(self):
        with self.assertRaises(ImproperlyConfigured):
            try:
                _validate_base_model()
            except:
                pass
            else:
                raise Exception

    @override_settings(BASE_MODEL_DEFAULT=CustomNonAbstractBaseModel)
    def test_is_custom_base_model_abstract(self):
        self.assertRaises(ImproperlyConfigured, _validate_base_model)

    @override_settings(BASE_MODEL_DEFAULT=CustomNonAbstractBaseModel)
    def test_base_model_abstract_message(self):
        self.assertRaisesMessage(ImproperlyConfigured, 'BASE_MODEL_DEFAULT should be an abstract class',
                                 _validate_base_model)

    # def test_base_model_inheritance(self):
    #     self.assertRaisesMessage(ImproperlyConfigured, 'User defined models should proxy BaseModel',
    #                              _validate_model_inheritance)
