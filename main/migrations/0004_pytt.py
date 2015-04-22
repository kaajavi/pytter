# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_auto_20150421_1132'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pytt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('funciona', models.BooleanField(verbose_name=b'Funciona?')),
                ('codigo', models.TextField(verbose_name=b'C\xc3\xb3digo')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('autor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
