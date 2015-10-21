from django.core.mail import send_mail
from celery import task

@task()
def send_comment_mail(subject, message, from_email, to_list, **kwargs):
    send_mail(subject, message, from_email, to_list, **kwargs)
