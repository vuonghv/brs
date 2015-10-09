from django.db import models
from django.conf import settings


def _path_to_avatar(instance, filename):
    return '{user_id}/{dirname}/{filename}'.format(
                        user_id=instance.user.id,
                        dirname=settings.AVATAR_DIR_NAME,
                        filename=filename)


class UserProfile(models.Model):
    """
    User's profile adding more information for Django Auth User
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True, related_name='profile')
    #avatar = models.ImageField(upload_to=_path_to_avatar, blank=True, default='', max_length=257)
    followers = models.ManyToManyField('self', through='FollowShip',
                                through_fields=('followee', 'follower'),
                                related_name='following', symmetrical=False)


class FollowShip(models.Model):
    follower = models.ForeignKey(UserProfile, related_name='follower')
    followee = models.ForeignKey(UserProfile, related_name='followee')
    time = models.DateTimeField(auto_now=True)
