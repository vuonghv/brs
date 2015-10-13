# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('books', '0002_auto_20151009_0344'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(max_length=255, upload_to='books', blank=True, default=''),
        ),
        migrations.AddField(
            model_name='book',
            name='user_profile',
            field=models.ManyToManyField(to='users.UserProfile', related_name='book', through='books.UserProfileBook'),
        ),
    ]
