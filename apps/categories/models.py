from django.db import models


class Category(models.Model):
    title = models.CharField(blank=False, max_length=257)
    description = models.TextField(blank=True, default='')
