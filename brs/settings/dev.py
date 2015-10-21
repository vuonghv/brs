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
