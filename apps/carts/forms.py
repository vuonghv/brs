from django import forms

from apps.carts.models import Cart


class BookItemForm(forms.Form):
    book = forms.IntegerField()
    quantity = forms.IntegerField(min_value=0)


class BookForm(forms.Form):
    book = forms.IntegerField()


class CartForm(forms.ModelForm):

    class Meta:
        model = Cart
        fields = ('phone', 'shipping_address')
