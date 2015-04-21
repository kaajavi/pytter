# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('birth_date', models.DateField(verbose_name=b'Fecha de Nacimiento', blank=True)),
                ('genre', models.CharField(blank=True, max_length=1, verbose_name=b'Soy', choices=[(b'm', b'Programador'), (b'f', b'Programadora')])),
                ('web', models.URLField(verbose_name=b'Blog/Web', blank=True)),
                ('twitter', models.CharField(max_length=200, verbose_name=b'Twitter', blank=True)),
                ('googleplus', models.CharField(max_length=200, verbose_name=b'Google+', blank=True)),
                ('avatar', models.FileField(upload_to=b'image/', verbose_name=b'Avatar')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
