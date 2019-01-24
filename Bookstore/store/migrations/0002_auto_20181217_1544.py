# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='Books',
            name='Prize',
            field=models.DecimalField(default=0.0, max_digits=8, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='Books',
            name='stack',
            field=models.IntegerField(default=0),
        ),
    ]
