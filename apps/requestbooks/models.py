from django.db import models

from apps.users.models import UserProfile
from apps.categories.models import Category


class RequestedBook(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, default='')
    user_profile = models.ForeignKey(UserProfile)
    requested_time = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, related_name='requests')

    class Meta:
        db_table = 'request'
