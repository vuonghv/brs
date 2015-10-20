from django.db import models

from apps.books.models import Book
from apps.users.models import UserProfile


class Cart(models.Model):
    WAITING = 1
    CANCELLED = 2
    COMPLETED = 3

    STATUS_CHOICES = (
        (WAITING, 'Waiting'),
        (CANCELLED, 'Cancelled'),
        (COMPLETED, 'Completed'),
    )

    user_profile = models.ForeignKey(UserProfile, related_name='carts')
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=WAITING)
    created_date = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=255)
    shipping_address = models.CharField(max_length=300)

    def get_total_price(self):
        try:
            total_price = 0
            list = self.items.all()
            for item in list:
                total_price += item.quantity * item.product.price            
        except Exception:
            return 0
        return total_price

class Item(models.Model):
    product = models.ForeignKey(Book, related_name='items')
    cart = models.ForeignKey(Cart, related_name='items')
    quantity = models.PositiveIntegerField()

    def get_price(self):
        return self.product.price * self.quantity
