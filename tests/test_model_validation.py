from django.test import SimpleTestCase


# from django.test.utils import override_settings
from django.test import override_settings

from django_base_model.apps import _validate_custom_base_model
from tests import test_app


class ModelValidTests(SimpleTestCase):

    # @override_settings(CORS_ORIGIN_ALLOW_ALL=object)
    def test_is_default_base_model_abstract(self):
        self.assertRaisesMessage(Exception, _validate_custom_base_model)

    @override_settings(DEFAULT_BASE_MODEL=test_app.models.CustomAbstractBaseModel)
    def test_is_custom_base_model_abstract(self):
        self.assertRaises(Exception, _validate_custom_base_model)

    def test_base_model_abstract_message(self):
        self.assertRaisesMessage(Exception, 'DEFAULT_BASE_MODEL should be abstract class', _validate_custom_base_model)
        # with self.assertRaises(Exception) as context:
        #     _validate_custom_base_model()
        # self.assertTrue('DEFAULT_BASE_MODEL should be abstract class' in context.exception)

    def test_all_models_inherits(self):
        pass
