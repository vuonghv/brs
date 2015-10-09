from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import ListView, DetailView
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

class DetaiView(BaseView, DetailView):
    """docstring for DetaiView"""
    model = Book
    template_name = 'books/detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        info = {
            'title': 'Book Review System'
        }
        context.update(info)
        return context

