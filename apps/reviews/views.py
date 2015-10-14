from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import (
        ListView, DetailView, TemplateView, CreateView, FormView
)
from django.views.generic.detail import SingleObjectMixin
from django.core.exceptions import PermissionDenied

from apps.core.views import BaseView
from apps.books.models import Book   
from apps.reviews.models import Review
from apps.reviews.forms import ReviewBookForm
from apps.core.views import LoginRequiredMixin


class CreateReviewView(LoginRequiredMixin, SingleObjectMixin, FormView):
    model = Book
    form_class = ReviewBookForm

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return HttpResponseRedirect(self.get_success_url())

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if Review.objects.filter(book=self.object,
                user_profile=request.user.profile).exists():
            raise PermissionDenied("You've created review for this book")

        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('books:detail',
                            kwargs={'pk': self.object.pk,
                                    'slug': self.object.slug}) + '#info-reviews-' + str(self.review.pk)

    def form_valid(self, form):
        form.instance.book = self.object
        form.instance.user_profile = self.request.user.profile
        self.review = form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return HttpResponseRedirect(self.get_success_url())
