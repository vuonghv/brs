# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requestbooks', '0002_requestedbook_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestedbook',
            name='status',
            field=models.IntegerField(choices=[(1, 'Waiting'), (2, 'Canceled'), (3, 'Approved'), (4, 'Disapproved')], default=1),
        ),
    ]
