from django.db import models


class Comment(models.Model):
    user_profile = models.ForeignKey(UserProfile)
    review = models.ForeignKey(Review)
    content = models.TextField()
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comment'
