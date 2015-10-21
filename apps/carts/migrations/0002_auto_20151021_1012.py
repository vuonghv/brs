# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='status',
            field=models.SmallIntegerField(choices=[(1, 'Waiting'), (2, 'Cancelled'), (3, 'Completed')], default=1),
        ),
    ]
