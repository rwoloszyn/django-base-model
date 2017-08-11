from django.test import SimpleTestCase
from django.test.utils import override_settings

from django_base_model.conf import conf


class ConfTests(SimpleTestCase):

    @override_settings(BASE_MODEL_DEFAULT=['tingtangtong'])
    def test_can_override(self):
        assert conf.BASE_MODEL_DEFAULT == ['tingtangtong']
