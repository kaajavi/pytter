from django.conf.urls import patterns, include, url
from pytter import settings
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

urlpatterns = patterns('',
                       url(r'^$', 'main.views.home', name='home'),               
                       url(r'^loguearse/$', 'main.views.loguearse', name='loguearse'),
                       url(r'^desloguearse/$', 'main.views.desloguearse', name='desloguearse'),
                       url(r'^pytt/ejecutar$', 'main.views.ejecutar', name='ejecutar'), 
                       url(r'^pytt/guardar$', 'main.views.add_pytt', name='add_pytt'), 
                       url(r'^user/edit_social_profile/$', 'main.views.edit_social_profile', name='edit_social_profile'),
                       url('^register/', 'main.views.registro', name='registro'),
                      )