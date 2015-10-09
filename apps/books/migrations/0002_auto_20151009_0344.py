# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
        ('users', '0001_initial'),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofilebook',
            name='user_profile',
            field=models.ForeignKey(to='users.UserProfile'),
        ),
        migrations.AddField(
            model_name='book',
            name='categories',
            field=models.ManyToManyField(to='categories.Category', db_table='category_book', related_name='books'),
        ),
        migrations.AddField(
            model_name='book',
            name='favourites',
            field=models.ManyToManyField(to='users.UserProfile', db_table='favourites', related_name='liked_books'),
        ),
    ]
