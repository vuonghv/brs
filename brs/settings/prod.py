import dj_database_url
from brs.settings.base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
