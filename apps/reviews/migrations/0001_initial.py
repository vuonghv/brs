# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('content', models.TextField(default='', blank=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('rating', models.IntegerField(default=4, choices=[(1, 'One star'), (2, 'Two stars'), (3, 'Three stars'), (4, 'Four stars'), (5, 'Five stars')])),
                ('book', models.ForeignKey(to='books.Book')),
            ],
            options={
                'db_table': 'review',
            },
        ),
    ]
