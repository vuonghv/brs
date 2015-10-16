import os

from django.apps import AppConfig
from django.conf import settings


class BooksAppConfig(AppConfig):
    name = 'apps.books'
    verbose_name = "Books apps"

    def ready(self):
        if settings.DEBUG:
            book_dir = os.path.join(settings.MEDIA_ROOT, settings.BOOK_DIR)
            try:
                os.makedirs(book_dir, mode=0o700)
            except OSError as err:
                pass
