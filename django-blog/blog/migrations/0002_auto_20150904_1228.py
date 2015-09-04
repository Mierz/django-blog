# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categories',
            new_name='Categorie',
        ),
        migrations.RenameModel(
            old_name='Posts',
            new_name='Post',
        ),
    ]
