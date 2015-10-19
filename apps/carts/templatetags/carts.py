from django import template

from apps.carts.utils import get_cart


register = template.Library()

@register.simple_tag(takes_context=True)
def get_quantity(context, item_id):
    cart = get_cart(context['request'])
    return cart[str(item_id)]
