from django.shortcuts import render
from django.views.generic import ListView

from apps.books.models import Book

class HomePageView(ListView):
    """docstring for HomePageView"""
    template_name = 'books/index.html'
    model = Book

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['list_book'] = Book.objects.all()
        return context        