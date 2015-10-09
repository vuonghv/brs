# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=500)),
                ('author', models.CharField(max_length=255)),
                ('pages', models.IntegerField()),
                ('publish_date', models.DateTimeField()),
                ('description', models.TextField(default='', blank=True)),
            ],
            options={
                'db_table': 'book',
            },
        ),
        migrations.CreateModel(
            name='UserProfileBook',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('status', models.IntegerField(default=1, choices=[(1, 'Reading'), (2, 'Read')])),
                ('book', models.ForeignKey(to='books.Book')),
            ],
            options={
                'db_table': 'user_book',
            },
        ),
    ]
