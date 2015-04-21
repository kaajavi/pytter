# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150420_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.FileField(default=b'image/noAvatar.png', upload_to=b'image/', verbose_name=b'Avatar'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='googleplus',
            field=models.URLField(null=True, verbose_name=b'Google+', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='twitter',
            field=models.URLField(null=True, verbose_name=b'Twitter', blank=True),
        ),
    ]
