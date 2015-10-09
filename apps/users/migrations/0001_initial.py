# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowShip',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(serialize=False, related_name='profile', primary_key=True, to=settings.AUTH_USER_MODEL)),
                ('followers', models.ManyToManyField(through='users.FollowShip', to='users.UserProfile', related_name='following')),
            ],
        ),
        migrations.AddField(
            model_name='followship',
            name='followee',
            field=models.ForeignKey(related_name='followee', to='users.UserProfile'),
        ),
        migrations.AddField(
            model_name='followship',
            name='follower',
            field=models.ForeignKey(related_name='follower', to='users.UserProfile'),
        ),
    ]
