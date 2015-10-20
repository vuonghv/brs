from django.http import (
        HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
)
from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView, View
from django.views.generic.edit import FormView
from django.forms.formsets import formset_factory

from apps.core.views import BaseView
from apps.carts import utils
from apps.carts.forms import BookItemForm, BookForm
from apps.books.models import Book


class ViewCart(BaseView, FormView):
    template_name = 'carts/index.html'
    form_class = formset_factory(BookItemForm, extra=0)
    success_url = reverse_lazy('carts:view')

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
        return HttpResponseRedirect(reverse('books:detail',
                            kwargs={'pk': book_id, 'slug': book.slug}))


class UpdateBookToCart(FormView):
    form_class = BookItemForm

    def get(self, request, *args, **kwargs):
        return HttpResponseBadRequest()

    def form_valid(self, form):
        cart = utils.get_cart(self.request)
        book_id = form.cleanded_data['book']
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
        cart = utils.get_cart(self.request)
        book_id = form.cleanded_data['book']
        if hasattr(cart, str(book_id)):
            del cart[str(book_id)]

        self.request.session.modified = True
        book = get_object_or_404(Book, id=book_id)
        return HttpResponseRedirect(reverse('books:detail',
                            kwargs={'pk': book_id, 'slug': book.slug}))


class ClearCart(View):
    
    def get(self, request, *args, **kwargs):
        return HttpResponseBadRequest()

    def post(self, request, *args, **kwargs):
        cart = utils.get_cart(request)
        del cart
        request.session.modified = True
        return HttpResponseRedirect(reverse('carts:view'))
