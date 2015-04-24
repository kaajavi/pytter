#!/usr/bin/python
# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

'''
Esta clase no viene por defecto pero es muy importante para 

'''

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm, CharField


from django.forms.utils import ErrorList
from django.contrib.auth.models import User

from main.models import UserProfile, GENRE_CHOICES

from django.forms.utils import ErrorList
from main.widgets import MyFileInput

# import the logging library
import logging
# Instancia del logger
logger = logging.getLogger('django')


class DivErrorList(ErrorList):

    def __unicode__(self):  # __unicode__ on Python 2
        return self.as_divs()

    def as_divs(self):
        if not self:
            return ''
        return '<div class="alert alert-danger">%s</div>' \
            % ''.join(['<div class="alert-danger">%s</div>' % e
                      for e in self])
        
        
class MyUserCreationForm(UserCreationForm):
    error_css_class = 'alert alert-danger' 
    
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        for (field_name, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field.required:
                field.widget.attrs['placeholder'] = 'Requerido'
                field.label = '* ' + str(field.label)
        
    

class EditSocialProfileForm(forms.ModelForm):

    error_css_class = 'alert alert-danger'    
    genre = forms.ChoiceField(choices=GENRE_CHOICES, required=False,
                              label='Soy')    
    
    class Meta:

        model = UserProfile
        exclude = ('user', )
        

    def __init__(self, *args, **kwargs):
        super(EditSocialProfileForm, self).__init__(*args, **kwargs)
        for (field_name, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field.required:
                field.widget.attrs['placeholder'] = 'Requerido'
                field.label = '* ' + field.label                


