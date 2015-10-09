from django.db import models

from apps.users.models import UserProfile
from apps.reviews.models import Review

class Comment(models.Model):
    user_profile = models.ForeignKey(UserProfile)
    review = models.ForeignKey(Review)
    content = models.TextField()
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comment'
