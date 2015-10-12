from django.contrib.auth.models import User
from django import forms

from apps.books.models import *

class UserProfileBookForm(forms.ModelForm):
    """docstring for LoginForm"""
    class Meta:
        model = UserProfileBook
        fields = ['user_profile', 'book', 'status']