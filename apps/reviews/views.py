from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import (
        ListView, DetailView, TemplateView, CreateView
)
from django.db.models import Q

from apps.core.views import BaseView
from apps.books.models import Book   
from apps.reviews.models import Review


class CreateReviewView(BaseView, CreateView):
    model = Review
    template_name = 'books/index.html'
    fields = ['book', 'rating', 'content']

    def get_success_url(self):
        return reverse_lazy('books:detail',
                            kwargs={'pk': self.object.book.pk,
                                    'slug': self.object.book.slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Write a review'
        context['form'].fields['book'] = self.request.GET.get('book','')
        context['form'].fields['rating'] = self.request.GET.get('rating', 0)
        return context
