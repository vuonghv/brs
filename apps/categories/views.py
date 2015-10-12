

from django.views.generic import ListView, DetailView, TemplateView

from apps.core.views import BaseView
from apps.books.models import Book
from . import models

class ListCategoryView(BaseView, ListView):
    """docstring for ListCategoryView"""
    model = Book
    template_name = 'categories/index.html'
    context_object_name = 'list_book'

    def get_queryset(self):
        return Book.objects.filter(categories__id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(ListCategoryView, self).get_context_data(**kwargs)
        cur_category = models.Category.objects.get(id=self.kwargs['pk'])
        info = {
            'info': {
                'title': cur_category.name + ' -  Book Review'
            }
        }
        context.update(info)
        return context
        
