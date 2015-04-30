# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='list',
            field=models.TextField(default=b''),
        ),
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(default=b''),
        ),
    ]
