# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='body',
            field=models.TextField(default=datetime.datetime(2015, 9, 4, 14, 17, 36, 50135, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
