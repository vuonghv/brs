import traceback
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.core.urlresolvers import reverse
from celery import task

from apps.reviews.models import Review

@task()
def send_comment_mail(url, review_pk):
    try:
        review = Review.objects.get(pk=review_pk)
    except ObjectDoesNotExist as err:
        print(err.strerror)
        traceback.print_exc()
        return

    if not review.user_profile.user.email:
        return

    subject = '[BRS] Comment on Reiview'
    message = ('Someone has commented on your review.\n'
                'Please check {}.').format(url)
    to_list = [review.user_profile.user.email,]
    from_email = settings.EMAIL_HOST_USER
    send_mail(subject, message, from_email, to_list, fail_silently=False)
