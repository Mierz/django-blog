# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20150907_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='url',
            field=models.CharField(default=datetime.datetime(2015, 9, 7, 12, 47, 54, 56773, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
    ]
