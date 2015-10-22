import djcelery
from brs.settings.base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

djcelery.setup_loader()

BROKER_URL = 'django://'
