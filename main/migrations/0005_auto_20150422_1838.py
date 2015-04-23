# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_pytt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.FileField(default=b'image/noAvatar.png', upload_to=b'image/', verbose_name=b'Avatar', blank=True),
        ),
    ]
