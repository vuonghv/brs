import dj_database_url
from brs.settings.base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

THIRD_APPS = [
        'storages',
]

INSTALLED_APPS += THIRD_APPS

# For Amazon Web Services settings

AWS_STORAGE_BUCKET_NAME = os.environ.get('S3_BUCKET_NAME')

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')

AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

AWS_S3_CUSTOM_DOMAIN = '{}.s3.amazonaws.com'.format(AWS_STORAGE_BUCKET_NAME)

# For static files

STATICFILES_LOCATION = 'static'

STATICFILES_STORAGE = 'brs.custom_storages.StaticStorage'

STATIC_URL = 'https://{}/{}/'.format(AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)

# For media files

MEDIAFILES_LOCATION = 'media'

MEDIA_URL = 'https://{}/{}/'.format(AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)

DEFAULT_FILE_STORAGE = 'brs.custom_storages.MediaStorage'
