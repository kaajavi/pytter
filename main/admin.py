# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.utils.translation import ugettext_lazy



# Register your models here.
from main.models import UserProfile, Pytt

admin.site.register(UserProfile)
admin.site.register(Pytt)