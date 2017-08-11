import django
from django.conf import global_settings

SECRET_KEY = 'NOTASECRET'

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_base_model',
    'tests.test_app',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'TEST_NAME': ':memory:',
    },
}

ROOT_URLCONF = 'tests.urls'


middlewares = list(global_settings.MIDDLEWARE_CLASSES)
# middlewares.append('corsheaders.middleware.CorsMiddleware')

if django.VERSION >= (1, 10):
    MIDDLEWARE = middlewares
else:
    MIDDLEWARE_CLASSES = middlewares

SECURE_PROXY_SSL_HEADER = ('HTTP_FAKE_SECURE', 'true')