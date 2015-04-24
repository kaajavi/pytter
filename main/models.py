#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.auth.models import User
# Create your models here.


GENRE_CHOICES = (('m', 'Programador'), ('f', 'Programadora'))

class Pytt(models.Model):
    
    class Meta:
        ordering = ['-upload_date']
        verbose_name = 'Pytt'
        verbose_name_plural = 'Pytters'
    
    funciona = models.BooleanField('Funciona?', default=False)
    warnings = models.BooleanField('Warnings?', default=False)
    title = models.CharField('Título', max_length=64, default='')
    autor= models.ForeignKey(settings.AUTH_USER_MODEL) 
    codigo= models.TextField('Código')
    upload_date = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.upload_date.strftime('%d/%m/%y %H:%M') + ' -> ' + str(self.autor)

class UserProfile(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    birth_date = models.DateField('Fecha de Nacimiento', null=True,
                                  blank=True)
    genre = models.CharField('Soy', max_length=1,
                             choices=GENRE_CHOICES, null=True,
                             blank=True)
    web = models.URLField('Blog/Web', max_length=200, null=True,
                          blank=True)
    twitter = models.URLField('Twitter', max_length=200, null=True,
                               blank=True)
    googleplus = models.URLField('Google+', max_length=200, null=True,
                                  blank=True)
    avatar = models.FileField('Avatar', upload_to='image/',
                              default='image/noAvatar.png', blank=True)
    
    upload_date = models.DateTimeField(auto_now_add=True)

    def genre_icon(self):
        if self.genre == 'm':
            return 'male'
        elif self.genre == 'f':
            return 'female'
        else:
            return 'neuter'
    
    
    def __unicode__(self):
        return self.user


def create_user_profile(
    sender,
    instance,
    created,
    **kwargs
    ):

    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(create_user_profile, sender=User)
