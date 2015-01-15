# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20150112_2254'),
    ]

    operations = [
        migrations.AddField(
            model_name='newpage',
            name='date',
            field=models.DateField(verbose_name='Publicación', default=datetime.datetime(2015, 1, 14, 18, 47, 7, 31391, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='date',
            field=models.DateField(verbose_name='Publicación'),
            preserve_default=True,
        ),
    ]
