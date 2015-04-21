from django.conf.urls import patterns, include, url
from pytter import settings


urlpatterns = patterns('',
                       url(r'^$', 'main.views.home', name='home'),               
                       url(r'^loguearse/$', 'main.views.loguearse', name='loguearse'),
                       url(r'^desloguearse/$', 'main.views.desloguearse', name='desloguearse'),
                       url(r'^function/alguna$', 'main.views.ejecutar', name='ejecutar'), 
                       url(r'^user/edit_social_profile/$', 'main.views.edit_social_profile', name='edit_social_profile'),
                      )