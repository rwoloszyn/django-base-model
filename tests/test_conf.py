import django
from django.test import SimpleTestCase
from django.test.utils import override_settings

from django_base_model import conf


class ConfTests(SimpleTestCase):

    @classmethod
    def setUpClass(cls):
        super(ConfTests, cls).setUpClass()
        django.setup()

    @override_settings(DEFAULT_BASE_MODEL=['tingtangtong'])
    def test_can_override(self):
        assert conf.DEFAULT_BASE_MODEL == ['tingtangtong']
