from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView

from apps.core.views import BaseView
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

class DetaiBookView(BaseView, DetailView):
    """docstring for DetaiView"""
    model = Book
    template_name = 'books/detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetaiBookView, self).get_context_data(**kwargs)
        info = {
            'info': {
                'title': self.object.title
            }
        }
        context.update(info)
        return context

