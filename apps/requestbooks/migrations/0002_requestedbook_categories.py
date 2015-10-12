# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('requestbooks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestedbook',
            name='categories',
            field=models.ManyToManyField(related_name='requests', to='categories.Category'),
        ),
    ]
