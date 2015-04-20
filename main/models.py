# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class UserProfile(models.Model):

    GENRE_CHOICES = (
        ('m', 'Programador'),
        ('f', 'Programadora'),
    )
    

    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    birth_date = models.DateField()
    genre = models.CharField(max_length=1, choices=GENRE_CHOICES)
    
    


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

        

        
post_save.connect(create_user_profile, sender=User)
