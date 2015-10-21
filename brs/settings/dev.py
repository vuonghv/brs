import djcelery
from brs.settings.base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

djcelery.setup_loader()

BROKER_URL = 'django://'

THIRD_APPS = [
        'djcelery',
        'kombu.transport.django',
]

INSTALLED_APPS += THIRD_APPS

# Settings for sending emails
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'vuonghv.cs@gmail.com'
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
