from django.http import (
        HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
)
from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView, View
from django.views.generic.edit import FormView
from django.forms.formsets import formset_factory
from django.contrib import messages

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from apps.core.views import BaseView
from apps.carts import utils
from apps.carts.forms import BookItemForm, BookForm
from apps.books.models import Book


class ViewCart(BaseView, FormView):
    template_name = 'carts/index.html'
    form_class = formset_factory(BookItemForm, extra=0)
    success_url = reverse_lazy('carts:view')
    
    def get_context_data(self, **kwargs):
        context = super(ViewCart, self).get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Cart - Book Review System'
            }
        }
        context.update(info)
        return context

    def get_initial(self):
        cart = utils.get_cart(self.request)
        initial = [{'book': k, 'quantity': v} for k, v in cart.items()]
        return initial

    def form_valid(self, form):
        cart = utils.get_cart(self.request)
        formset = form
        for form in formset:
            book_id = form.cleaned_data['book']
            quantity = form.cleaned_data['quantity']
            cart.update({str(book_id): quantity})

        self.request.session.modified = True
        messages.success(self.request, "Cart is updated successfully!",
                            extra_tags='woocommerce-message')
        return HttpResponseRedirect(self.success_url)

class AddBookToCart(FormView):
    form_class = BookItemForm

    def get(self, request, *args, **kwargs):
        return HttpResponseBadRequest()
    
    def form_valid(self, form):
        cart = utils.get_cart(self.request)
        book_id = form.cleaned_data['book']
        quantity = form.cleaned_data['quantity']
        exist = cart.get(str(book_id))

        if exist is not None:
            cart[str(book_id)] += quantity
        else:
            cart[str(book_id)] = quantity
        
        # Need for update session database
        self.request.session.modified = True

        book = get_object_or_404(Book, id=book_id)
        messages.success(self.request,
                    '"{}" has been added to your cart.'.format(book.title),
                    extra_tags='woocommerce-message')
        
        return HttpResponseRedirect(reverse('books:detail',
                            kwargs={'pk': book_id, 'slug': book.slug}))

class UpdateBookToCart(FormView):
    form_class = BookItemForm

    def get(self, request, *args, **kwargs):
        return HttpResponseBadRequest()

    def form_valid(self, form):
        cart = utils.get_cart(self.request)
        book_id = form.cleaned_data['book']
        quantity = form.cleaned_data['quantity']
        cart[str(book_id)] = quantity

        self.request.session.modified = True
        book = get_object_or_404(Book, id=book_id)
        return HttpResponseRedirect(reverse('books:detail',
                            kwargs={'pk': book_id, 'slug': book.slug}))

class RemoveBookFromCart(FormView):
    form_class = BookForm

    def get(self, request, *args, **kwargs):
        return HttpResponseBadRequest()

    def form_valid(self, form):
        book_id = form.cleaned_data['book']
        cart = utils.get_cart(self.request)
        book_id = form.cleaned_data['book']
        if str(book_id) in cart.keys():
            del cart[str(book_id)]

        self.request.session.modified = True
        book = get_object_or_404(Book, id=book_id)
        messages.success(self.request,
                    '"{}" has been removed from your cart.'.format(book.title),
                    extra_tags='woocommerce-message')
        return HttpResponseRedirect(reverse('carts:view'))


class ClearCart(View):
    
    def get(self, request, *args, **kwargs):
        return HttpResponseBadRequest()

    def post(self, request, *args, **kwargs):
        cart = utils.get_cart(request)
        del cart
        request.session.modified = True
        return HttpResponseRedirect(reverse('carts:view'))

class CheckOutView(BaseView, TemplateView):
    """docstring for CheckOutView"""
    template_name = "carts/checkout.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(CheckOutView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CheckOutView, self).get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Checkout - Book Review System'
            }
        }
        context.update(info)
        return context
        
