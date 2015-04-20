'''
Esta clase no viene por defecto pero es muy importante para 

'''

# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm, CharField
from myapp.models import Article
from django.contrib.admin.widgets import AdminDateWidget 
from django.forms.utils import ErrorList
from django.contrib.auth import User

class AddUserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', ' first_name', 'last_name', 'email','password')
        labels = {
            'username': _('Nombre de usuario'),
        }
        help_texts = {
            'name': _('Some useful help text.'),
        }
        error_messages = {
            'name': {
                'max_length': _("This writer's name is too long."),
            },
        }