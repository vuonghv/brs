from django import template

from apps.carts.utils import get_cart
from apps.books.models import Book

register = template.Library()

@register.simple_tag(takes_context=True)
def get_quantity(context, item_id):
    cart = get_cart(context['request'])
    return cart[str(item_id)]

@register.simple_tag(takes_context=True)
def get_one_book_total_price(context, item_id):
    try:
        cart = get_cart(context['request'])
        book = Book.objects.get(id=item_id)
        total_price = book.price * cart[str(item_id)]
    except Exception:
        total_price = 0
    return total_price

@register.simple_tag(takes_context=True)
def get_total_price(context):
    try:
        total_price = 0
        cart = get_cart(context['request'])
        for key, value in cart.items():
            book = Book.objects.get(id=key)
            total_price += (book.price * int(value))
    except Exception:
        total_price = 0
    return total_price