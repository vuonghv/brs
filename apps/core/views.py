from django.views.generic.detail import ContextMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Count

from apps.categories.models import Category
from apps.books.models import Book, UserProfileBook
from apps.reviews.models import Review

class BaseView(ContextMixin):
    """docstring for BaseView"""
    model = Book
    def get_context_data(self, **kwargs):
        context = super(BaseView, self).get_context_data(**kwargs)
        info = {
            'list_book_recommendations': Book.objects.annotate(
                Count('favourites')).order_by('-favourites__count')[0:5],
            'list_top_review': Book.objects.annotate(
                Avg('review__rating')).order_by('-review__rating__avg')[0:5],
            'list_category': Category.objects.all()
        }
        context.update(info)
        return context


class LoginRequiredMixin(object):
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
