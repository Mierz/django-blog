# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150904_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default=datetime.datetime(2015, 9, 4, 12, 35, 55, 752420, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
