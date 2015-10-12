from django.db import models

from apps.categories.models import Category
from apps.users.models import UserProfile
from apps.reviews.models import Review


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

    def get_rating(self):
        reviews = Review.objects.filter(book=self)
        total = reviews.count()
        rating = 0
        for review in reviews:
            rating += review.rating
        return round(rating / total)


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
