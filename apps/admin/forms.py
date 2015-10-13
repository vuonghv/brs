from django.contrib.auth.models import User
from django import forms

from apps.categories.models import *
from apps.books.models import *

class LoginForm(forms.ModelForm):
    """docstring for LoginForm"""
    class Meta:
        model = User
        fields = ['username', 'password']

class CategoryForm(forms.ModelForm):
        """docstring for CategoryForm"""
        class Meta:
            model = Category
            fields = '__all__'

class BookForm(forms.ModelForm):
    """docstring for BookForm"""
    class Meta:
        model = Book
        fields = ('title', 'description', 'slug', 'categories',
                    'pages', 'author', 'publish_date', 'cover')
