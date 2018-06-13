# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_auto_20180430_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='top_name',
            field=models.CharField(unique=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='webpage',
            name='name',
            field=models.CharField(unique=True, max_length=255),
        ),
    ]
