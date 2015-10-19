# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('books', '0005_book_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('status', models.SmallIntegerField(choices=[(1, 'Waiting'), (2, 'Cancelled'), (3, 'Completed')])),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('phone', models.CharField(max_length=255)),
                ('shipping_address', models.CharField(max_length=300)),
                ('user_profile', models.ForeignKey(related_name='carts', to='users.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('quantity', models.PositiveIntegerField()),
                ('cart', models.ForeignKey(related_name='items', to='carts.Cart')),
                ('product', models.ForeignKey(related_name='items', to='books.Book')),
            ],
        ),
    ]
