from django.db import models

from apps.users.models import UserProfile
from apps.books.models import Book


class Review(models.Model):
    user_profile = models.ForeignKey(UserProfile)
    book = models.ForeignKey(Book)
    content = models.TextField(blank=True, default='')
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'review'
