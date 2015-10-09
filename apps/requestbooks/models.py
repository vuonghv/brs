from django.db import models

from apps.users.models import UserProfile


class RequestedBook(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, default='')
    user_profile = models.ForeignKey(UserProfile)
    requested_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'request'
