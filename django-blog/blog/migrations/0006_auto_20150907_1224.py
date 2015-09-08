# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_page_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='seo_description',
            field=models.CharField(default=datetime.datetime(2015, 9, 7, 12, 24, 43, 655427, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='seo_keywords',
            field=models.CharField(default=datetime.datetime(2015, 9, 7, 12, 24, 50, 7502, tzinfo=utc), max_length=80),
            preserve_default=False,
        ),
    ]
