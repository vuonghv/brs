from django import forms


class BookItemForm(forms.Form):
    book = forms.IntegerField()
    quantity = forms.IntegerField(min_value=0)


class BookForm(forms.Form):
    book = forms.IntegerField()
