# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestedBook',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, default='')),
                ('requested_time', models.DateTimeField(auto_now_add=True)),
                ('user_profile', models.ForeignKey(to='users.UserProfile')),
            ],
            options={
                'db_table': 'request',
            },
        ),
    ]
