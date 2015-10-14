from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import FormView, DeleteView, UpdateView
from django.core.urlresolvers import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseRedirect

from apps.reviews.models import Review
from apps.comments.models import Comment
from apps.reviews.models import Review
from apps.comments.forms import CommentReviewForm
from apps.core.views import LoginRequiredMixin


class CommentReviewView(LoginRequiredMixin, SingleObjectMixin, FormView):
    model = Review
    form_class = CommentReviewForm
    pk_url_kwarg = 'review'

    def get_success_url(self):
        return reverse_lazy('books:detail',
                    kwargs={'pk': self.object.book.pk,
                            'slug': self.object.book.slug}) + '#info-comment-' + self.comment.pk
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return HttpResponseRedirect(self.get_success_url())

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)


    def form_valid(self, form):
        form.instance.user_profile = self.request.user.profile
        form.instance.review = self.object
        self.comment = form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return HttpResponseRedirect(self.get_success_url())


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user_profile != request.user.profile:
            raise PermissionDenied('You do NOT own this comment')
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('books:detail',
                kwargs={'pk': self.object.review.book.pk,
                        'slug': self.object.review.book.slug}) + '#reviews'

    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(self.get_success_url())


class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    template_name = 'comments/update.html'
    fields = ['content',]

    def get_success_url(self):
        return reverse_lazy('books:detail',
                kwargs={'pk': self.object.review.book.pk,
                        'slug': self.object.review.book.slug}) + '#info-comment-' + str(self.object.pk)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user_profile != request.user.profile:
            raise PermissionDenied('You do NOT own this comment')
        return super().post(request, *args, **kwargs)
