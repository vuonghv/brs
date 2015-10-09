from django.dispatch import receiver
from django.db.models.signals import post_delete, post_save
from django.contrib.auth.signals import user_logged_in
from django.conf import Settings
from django.apps import apps

from users.models import UserProfile


@receiver(post_save, sender=apps.get_model(Settings.AUTH_USER_MODEL))
def create_user_profile(sender, instance, created, **kwargs):
    if not created:
        return
    profile = UserProfile.objects.create(user=instance)
    profile.save()

@receiver(user_logged_in, sender=apps.get_model(settings.AUTH_USER_MODEL))
def set_session_expiry(sender, request, user, **kwargs):
    pass
