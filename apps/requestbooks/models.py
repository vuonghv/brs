from django.db import models

from apps.users.models import UserProfile
from apps.categories.models import Category


class RequestedBook(models.Model):
    WAITING = 1
    CANCELED = 2
    APPROVED = 3
    DISAPPROVED = 4
    STATUS_CHOICES = (
            (WAITING, 'Waiting'),
            (CANCELED, 'Canceled'),
            (APPROVED, 'Approved'),
            (DISAPPROVED, 'Disapproved'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, default='')
    user_profile = models.ForeignKey(UserProfile)
    requested_time = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, related_name='requests')
    status = models.IntegerField(choices=STATUS_CHOICES, default=WAITING)

    class Meta:
        db_table = 'request'

    def __str__(self):
        return self.title

    def is_canceled(self):
        return self.status == RequestedBook.CANCELED

    def is_waiting(self):
        return self.status == RequestedBook.WAITING
