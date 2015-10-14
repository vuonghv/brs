from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, FormView, CreateView, UpdateView, View
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.views.generic.detail import SingleObjectMixin

from apps.books.forms import *
from apps.core.views import BaseView
from apps.books.models import Book, UserProfileBook
from apps.reviews.views import CreateReviewView
from apps.reviews.models import Review
from apps.users.models import FollowShip, UserProfile


class HomePageView(BaseView, ListView):
    """docstring for HomePageView"""
    template_name = 'books/index.html'
    model = Book
    context_object_name = 'list_book'

    def get_queryset(self):
        return Book.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        info = {
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
            },
            'favourite': self.object.favourites.filter(user=self.request.user).exists(),
        }
        context.update(info)
        context['reviews'] = Review.objects.filter(
                                book=self.object
                                ).order_by('-updated_time')
        if self.request.user.is_authenticated():
            context['status_review'] = Review.objects.filter(
                                    book=self.object,
                                    user_profile=self.request.user.profile).exists()
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
        return Book.objects.order_by('-favourites', '-id')

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
        return Book.objects.filter(
            Q(title__icontains=string_search) | 
            Q(categories__name__icontains=string_search)).distinct().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(SearchBookView, self).get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Search Books - Book Review'
            }
        }
        context.update(info)
        return context

class ListHistoryBookView(BaseView, ListView):
    """docstring for ListHistoryBookView"""
    model = User
    template_name = 'books/history.html'
    context_object_name = 'list_user_profile_book'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ListHistoryBookView, self).dispatch(request, *args, **kwargs)
        
    def get_queryset(self):
        return UserProfileBook.objects.filter(
                user_profile__user__username=self.kwargs['username']).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(ListHistoryBookView, self).get_context_data(**kwargs)
        info = {
            'history_user': User.objects.get(username=self.kwargs['username']),
            'is_followed': FollowShip.objects.filter(
                        follower=self.request.user.profile,
                        followee__user__username=self.kwargs['username']).exists(),

            'info': {
                'title': 'History Book Review'
            }
        }
        context.update(info)
        return context

class FavoriteBookView(View, SingleObjectMixin):
    model = Book

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(FavoriteBookView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.favourites.add(request.user.profile)
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('books:detail', kwargs={'pk': self.object.id, 'slug': self.object.slug})

class RemoveFavoriteBookView(View, SingleObjectMixin):
    model = Book

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(RemoveFavoriteBookView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.favourites.remove(request.user.profile)
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('books:detail', kwargs={'pk': self.object.id, 'slug': self.object.slug})

class ReadBookView(CreateView):
    """docstring for ReadBookView"""
    model = UserProfileBook
    form_class = UserProfileBookForm

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ReadBookView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('books:detail', kwargs={'pk': self.object.book.id, 'slug': self.object.book.slug})
    
class UpdateReadBookView(UpdateView):
    """docstring for UpdateReadBookView"""
    model = UserProfileBook
    form_class = UserProfileBookForm
            
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(UpdateReadBookView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('books:detail', kwargs={'pk': self.object.book.id, 'slug': self.object.book.slug})
