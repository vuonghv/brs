from django.db import models

from apps.categories.models import Category
from apps.users.models import UserProfile


class Book(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=500)
    author = models.CharField(max_length=255)
    pages = models.IntegerField()
    publish_date = models.DateTimeField()
    description = models.TextField(blank=True, default='')
    categories = models.ManyToManyField(Category, db_table='category_book', related_name='books')
    favourites = models.ManyToManyField(UserProfile, db_table='favourites', related_name='liked_books')

    class Meta:
        db_table = 'book'


class UserProfileBook(models.Model):
    READING = 1
    READ = 2
    READING_STATUS = (
            (READING, 'Reading'),
            (READ, 'Read'),
    )

    user_profile = models.ForeignKey(UserProfile)
    book = models.ForeignKey(Book)
    status = models.IntegerField(choices=READING_STATUS, default=READING)

    class Meta:
        db_table = 'user_book'
