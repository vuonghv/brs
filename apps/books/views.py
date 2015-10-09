from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import ContextMixin

from apps.core.views import BaseView
from apps.categories.models import Category
from apps.books.models import Book   

class HomePageView(BaseView, ListView):
    """docstring for HomePageView"""
    template_name = 'books/index.html'
    model = Book

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        info = {
            'list_book': Book.objects.order_by('-id'),
            'info': {
                'title': 'Book Review System'
            }
        }
        context.update(info)
        return context     

