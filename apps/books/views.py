from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, FormView
from django.db.models import Q

from apps.core.views import BaseView
from apps.books.models import Book   
from apps.reviews.views import CreateReviewView
from apps.reviews.models import Review

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
        context['reviews'] = Review.objects.filter(
                                book=self.object
                                ).order_by('-updated_time')
        return context

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CreateReviewView.as_view()
        return view(request, *args, **kwargs)

class RecommendationsBookView(BaseView, ListView):
    """docstring for RecommendationsBookView"""
    model = Book
    context_object_name = 'list_book'
    template_name = 'books/index.html'

    def get_queryset(self):
        return Book.objects.order_by('-id', 'favourites')

    def get_context_data(self, **kwargs):
        context = super(RecommendationsBookView, self).get_context_data(**kwargs)
        info = {
            'info': {
                'title': "Recommendations - Book Review"
            }
        }
        context.update(info)
        return context
        

class SearchBookView(BaseView, ListView):
    """docstring for SearchBookView"""
    model = Book
    template_name = 'books/index.html'
    context_object_name = 'list_book'

    def get_queryset(self):
        string_search = self.request.GET.get('s', None)
        return Book.objects.filter(Q(title__icontains=string_search) | Q(categories__name__icontains=string_search)).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(SearchBookView, self).get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Search Books - Book Review'
            }
        }
        context.update(info)
        return context

class FavoriteBookView(BaseView, FormView):
    """docstring for FavoriteBookView"""
    def __init__(self, arg):
        super(FavoriteBookView, self).__init__()
        self.arg = arg
        

class ReadBookView(BaseView):
    """docstring for ReadBookView"""
    def __init__(self, arg):
        super(ReadBookView, self).__init__()
        self.arg = arg
        
