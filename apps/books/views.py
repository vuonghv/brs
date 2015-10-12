from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, FormView, CreateView, UpdateView
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from apps.books.forms import *
from apps.core.views import BaseView
from apps.books.models import Book, UserProfileBook
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
        if self.request.user.is_authenticated():
            try:
                context['status_read'] = UserProfileBook.objects.get(
                                    book=self.object,
                                    user_profile=self.request.user.profile)
            except UserProfileBook.DoesNotExist:
                context['status_read'] = None

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
        
class UpdateReadBookView(BaseView, UpdateView):
    """docstring for UpdateReadBookView"""
    model = UserProfileBook
    form_class = UserProfileBookForm
        
    def get_success_url(self):
        id = self.request.POST.get('book', None)
        slug = self.request.POST.get('slug', None)
        return reverse('books:detail', kwargs={'pk': id, 'slug': slug})

class ReadBookView(BaseView, CreateView):
    """docstring for ReadBookView"""
    model = UserProfileBook
    form_class = UserProfileBookForm

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ReadBookView, self).dispatch(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     if UserProfileBook.filter(book__id=self.request.POST.get('book', None),
    #                                 user_profile=request.user.profile).exists():
    #         super(UpdateReadBookView, self).post(request)

    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     self.object.course = self.course
    #     self.object.save()
    #     return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        id = self.request.POST.get('book', None)
        slug = self.request.POST.get('slug', None)
        return reverse('books:detail', kwargs={'pk': id, 'slug': slug})
    
        
