from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.admin.forms import AdminAuthenticationForm
from django.views.generic import FormView, View, CreateView, DetailView, UpdateView, DeleteView, TemplateView, ListView
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout

from . import forms
from apps.categories.models import Category
from apps.books.models import Book
from apps.requestbooks.models import RequestedBook
from apps.users.models import UserProfile

class BaseView(View):
    """docstring for BaseView"""
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(BaseView, self).dispatch(request, *args, **kwargs)        

############################################################################
############################################################################
############################################################################
# Login

class LoginView(FormView):
    form_class = AdminAuthenticationForm
    template_name = 'admin/login.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_active and user.is_staff:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('admin:dashboard')

    def form_valid(self, form):
        admin = form.get_user()
        login(self.request, admin)
        return super().form_valid(form)

############################################################################
############################################################################
############################################################################
# Dashboard

class DashboardView(BaseView, TemplateView):
    template_name = 'admin/dashboard_index.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        info = {
            'title': 'Dashboard - Book Review System',
            'sidebar': ['dashboard']
        }
        context['info'] = info
        return context

############################################################################
############################################################################
############################################################################
# Category

class CategoryView(BaseView, ListView):
    """docstring for CategoryView"""
    context_object_name = 'list_category'
    template_name = 'admin/category_index.html'    

    def get_queryset(self):
        return Category.objects.all()

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        info = {
            'title': 'Category - Book Review System',
            'sidebar': ['category']
        }
        context['info'] = info
        return context

class CategoryCreateView(BaseView, CreateView):
    """docstring for CategoryCreateView"""
    form_class = forms.CategoryForm    
    template_name = 'admin/category_create.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryCreateView, self).get_context_data(**kwargs)
        info = {
            'title': 'Create Category - Book Review System',
            'sidebar': ['category']
        }
        context['info'] = info
        return context

    def get_success_url(self):
        return reverse('admin:list_category')

class CategoryUpdateView(BaseView, UpdateView):
    """docstring for CategoryUpdateView"""
    model = Category
    form_class = forms.CategoryForm    
    template_name = 'admin/category_update.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryUpdateView, self).get_context_data(**kwargs)
        info = {
            'title': 'Update Category - Book Review System',
            'sidebar': ['category']
        }
        context['info'] = info
        return context

    def get_success_url(self):
        return reverse('admin:list_category')

class CategoryDeleteView(BaseView, DeleteView):
    """docstring for CategoryDeleteView"""
    model = Category

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('admin:list_category')

############################################################################
############################################################################
############################################################################
# Book

class BookView(BaseView, ListView):
    """docstring for BookView"""
    context_object_name = 'list_book'
    template_name = 'admin/book_index.html'    

    def get_queryset(self):
        return Book.objects.all()

    def get_context_data(self, **kwargs):
        context = super(BookView, self).get_context_data(**kwargs)
        info = {
            'title': 'Book - Book Review System',
            'sidebar': ['book']
        }
        context['info'] = info
        return context

class BookCreateView(BaseView, CreateView):
    """docstring for BookCreateView"""
    form_class = forms.BookForm    
    template_name = 'admin/book_create.html'

    def get_context_data(self, **kwargs):
        context = super(BookCreateView, self).get_context_data(**kwargs)
        info = {
            'title': 'Create Book - Book Review System',
            'sidebar': ['book']
        }
        context['info'] = info
        context['list_category'] = Category.objects.all()
        return context

    def get_success_url(self):
        return reverse('admin:list_book')

class BookUpdateView(BaseView, UpdateView):
    """docstring for BookUpdateView"""
    model = Book
    form_class = forms.BookForm    
    template_name = 'admin/book_update.html'

    def get_context_data(self, **kwargs):
        context = super(BookUpdateView, self).get_context_data(**kwargs)
        info = {
            'title': 'Update Book - Book Review System',
            'sidebar': ['book']
        }
        context['info'] = info
        context['list_category'] = Category.objects.all()
        return context

    def get_success_url(self):
        return reverse('admin:list_book')

class BookDeleteView(BaseView, DeleteView):
    """docstring for BookDeleteView"""
    model = Book

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('admin:list_book')

############################################################################
############################################################################
############################################################################
# Requested Book

class RequestedBookView(BaseView, ListView):
    """docstring for RequestedBookView"""
    context_object_name = 'list_requested_book'
    template_name = 'admin/requested_book_index.html'

    def get_queryset(self):
        return RequestedBook.objects.all()

    def get_context_data(self, **kwargs):
        context = super(RequestedBookView, self).get_context_data(**kwargs)
        info = {
            'title': 'Requested - Book Review System',
            'sidebar': ['requested_book']
        }
        context['info'] = info
        return context

class RequestedBookDeleteView(BaseView, DeleteView):
    """docstring for RequestedBookDeleteView"""
    model = RequestedBook

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('admin:list_requested_book')

class RequestedBookDetailView(BaseView, DetailView):
    """docstring for RequestedBookDetailView"""
    def __init__(self, arg):
        super(RequestedBookDetailView, self).__init__()
        self.arg = arg

############################################################################
############################################################################
############################################################################
# User

class UserProfileView(BaseView, ListView):
    """docstring for UserProfileView"""
    context_object_name = 'list_user'
    template_name = 'admin/user_profile_index.html'

    def get_queryset(self):
        return UserProfile.objects.all()

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        info = {
            'title': 'User - Book Review System',
            'sidebar': ['user']
        }
        context['info'] = info
        return context

class UserProfileDeleteView(BaseView, DeleteView):
    """docstring for UserProfileDeleteView"""
    model = User

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('admin:list_user')

class UserProfileDetailView(BaseView, DetailView):
    """docstring for UserProfileDetailView"""
    def __init__(self, arg):
        super(UserProfileDetailView, self).__init__()
        self.arg = arg
