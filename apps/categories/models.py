from django.db import models


class Category(models.Model):
    name = models.CharField(blank=False, max_length=255)
    description = models.TextField(blank=True, default='')

    class Meta:
        db_table = 'category'
