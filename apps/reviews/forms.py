from django.forms import ModelForm

from apps.reviews.models import Review

class ReviewBookForm(ModelForm):

    class Meta:
        model = Review
        fields = ('rating', 'content',)
