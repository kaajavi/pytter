from django.conf.urls import patterns, include, url
from pytter import settings


urlpatterns = patterns('',
                       url(r'^$', 'main.views.home', name='home'),                       
                       url(r'^function/alguna$', 'main.views.ejecutar', name='ejecutar'), 
                      )