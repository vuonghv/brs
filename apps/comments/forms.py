from django.forms import ModelForm

from apps.comments.models import Comment


class CommentReviewForm(ModelForm):

    class Meta:
        model = Comment
        fields = ('content',)
