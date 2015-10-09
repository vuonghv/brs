from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=500)
    author = models.CharField(max_length=255)
    pages = models.IntegerField()
