from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import FormView, DeleteView, UpdateView
from django.core.urlresolvers import reverse, reverse_lazy
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings

from apps.reviews.models import Review
from apps.comments.models import Comment
from apps.reviews.models import Review
from apps.comments.forms import CommentReviewForm
from apps.comments.tasks import send_comment_mail
from apps.core.views import LoginRequiredMixin


class CommentReviewView(LoginRequiredMixin, SingleObjectMixin, FormView):
    model = Review
    form_class = CommentReviewForm
    # pk_url_kwarg = 'review'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)    
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return HttpResponseRedirect(self.get_success_url())

    def form_valid(self, form):
        form.instance.user_profile = self.request.user.profile
        form.instance.review = self.object
        self.comment = form.save()
        
        # send email to review owner
        path = '{}#info-comment-{}'.format(
                    reverse('books:detail',
                            kwargs={'pk': self.object.book.pk,
                            'slug': self.object.book.slug}),
                    self.comment.pk)
        url = self.request.build_absolute_uri(path)
        send_comment_mail.delay(url, self.object.pk)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('books:detail',
                    kwargs={'pk': self.object.book.pk,
                            'slug': self.object.book.slug}) + '#info-comment-' + str(self.comment.pk)

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
