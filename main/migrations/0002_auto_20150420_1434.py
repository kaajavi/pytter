# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.FileField(default=b'media/image/noAvatar.png', upload_to=b'image/', verbose_name=b'Avatar'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birth_date',
            field=models.DateField(null=True, verbose_name=b'Fecha de Nacimiento', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='genre',
            field=models.CharField(blank=True, max_length=1, null=True, verbose_name=b'Soy', choices=[(b'm', b'Programador'), (b'f', b'Programadora')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='googleplus',
            field=models.CharField(max_length=200, null=True, verbose_name=b'Google+', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='twitter',
            field=models.CharField(max_length=200, null=True, verbose_name=b'Twitter', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='web',
            field=models.URLField(null=True, verbose_name=b'Blog/Web', blank=True),
        ),
    ]
