# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('comments', '0002_comment_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user_profile',
            field=models.ForeignKey(to='users.UserProfile'),
        ),
    ]
