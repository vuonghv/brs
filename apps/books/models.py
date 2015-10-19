from django.db import models
from django.conf import settings

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
    user_profile = models.ManyToManyField(UserProfile, through='UserProfileBook', related_name='book')
    cover = models.ImageField(upload_to=settings.BOOK_DIR, max_length=255, default='', blank=False)
    price = models.FloatField(null=False, blank=False, default=0.0)

    class Meta:
        db_table = 'book'

    def delete(self, using=None):
        super().delete(using)
        if self.cover:
            self.cover.delete()

    def get_rating(self):
        reviews = Review.objects.filter(book=self)        
        total = reviews.count()
        if total == 0:
            return 0
        rating = 0
        for review in reviews:
            rating += review.rating
        return round(rating / total)

    def get_cover_url(self):
        if self.cover:
            return self.cover.url
        return ''


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
