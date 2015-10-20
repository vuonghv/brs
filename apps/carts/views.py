from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from apps.core.views import BaseView
from apps.carts import utils
from apps.carts.forms import BookItem
from apps.books.models import Book


class ViewCart(BaseView, TemplateView):
    template_name = 'carts/index.html'


class AddBookToCart(FormView):
    form_class = BookItem

    def get(self, request, *args, **kwargs):
        return HttpResponse()
    
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
