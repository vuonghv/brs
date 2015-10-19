from django import forms


class BookItem(forms.Form):
    book = forms.IntegerField()
    quantity = forms.IntegerField(min_value=0)
