from django.views.generic.detail import ContextMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from apps.categories.models import Category
from apps.books.models import Book

class BaseView(ContextMixin):
    """docstring for BaseView"""
    model = Book
    def get_context_data(self, **kwargs):
        context = super(BaseView, self).get_context_data(**kwargs)
        info = {
            'list_book_recommendations': Book.objects.all()[0:5],
            'list_top_review': Book.objects.all()[0:5],
            'list_category': Category.objects.all()            
        }
        context.update(info)
        return context


class LoginRequiredMixin(object):
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        super().dispatch(request, *args, **kwargs)
