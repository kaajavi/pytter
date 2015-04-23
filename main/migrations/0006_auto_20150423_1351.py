# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20150422_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='pytt',
            name='title',
            field=models.CharField(default=b'', max_length=64, verbose_name=b'T\xc3\xadtulo'),
        ),
        migrations.AddField(
            model_name='pytt',
            name='warnings',
            field=models.BooleanField(default=False, verbose_name=b'Warnings?'),
        ),
        migrations.AlterField(
            model_name='pytt',
            name='funciona',
            field=models.BooleanField(default=False, verbose_name=b'Funciona?'),
        ),
    ]
