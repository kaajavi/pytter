#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.template.defaulttags import NowNode
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.decorators import login_required


# Models
from django.contrib.auth.models import User
from main.models import Pytt, UserProfile
# Forms
from main.forms import EditSocialProfileForm, MyUserCreationForm

##Errores
from django.http import Http404

##BASE DE DATOS
from django.db.models import Q

##MENSAJES A LA VISTA (Cuadros de alertas, info, warning, etc
from django.contrib import messages

##TIEMPOS
from datetime import date

# import the logging library
import logging

# Instancia del logger
logger = logging.getLogger('django')

# Imports propios
from main.functions import checkCode

# Create your views here.

@login_required(login_url='/loguearse')
def home(request):
    context = RequestContext(request)
    pytts = Pytt.objects.all()[:10]
    users = UserProfile.objects.all()[:10]
    return render_to_response('index.html', {'pytts':pytts, 'users':users}, context)

def registro(request):
    context = RequestContext(request)
    args={}
    if request.method =='POST':
        createUserForm = MyUserCreationForm(request.POST)    
        if createUserForm.is_valid():
            userform = createUserForm.save()
            userform.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, userform)                      
            return redirect('/')
    else:
        createUserForm = MyUserCreationForm()
    args['createUserForm'] = createUserForm
    return render_to_response('registro.html', args, context)
    
    

def loguearse(request):
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    createUserForm = MyUserCreationForm()
    args = {}
    args['createUserForm'] = createUserForm
    if request.method == 'POST':

        # Usuario y contrasena

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:

            # Is the account active? It could have been disabled.

            if user.is_active:

                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.

                login(request, user)
                messages.add_message(request, messages.SUCCESS,
                        'Bienvenido nuevamente')
                
                return redirect('/')
            else:

                # An inactive account was used - no logging in!

                messages.add_message(request, messages.ERROR,
                        'Este usuario no está disponible!')
                return render_to_response('loguin.html', args, context)
        else:

            # Bad login details were provided. So we can't log the user in.

            messages.add_message(request, messages.ERROR,
                                 'No existe este usuario!')
            return render_to_response('login.html', args, context)
    else:

        # The request is not a HTTP POST, so display the login form.
        # This scenario would most likely be a HTTP GET.
    # No context variables to pass to the template system, hence the
    # blank dictionary object...

        return render_to_response('login.html',args, context)


def desloguearse(request):
    logout(request)
    context = RequestContext(request)
    messages.add_message(request, messages.SUCCESS, 'Muchas gracias!')
    return redirect('/')


@login_required(login_url='/loguearse')
def edit_social_profile(request):
    args = {}
    context = RequestContext(request)
    try:
        user = request.user
    except User.DoesNotExist:
        raise Http404('El usuario no existe')

    if request.method == 'POST':                
        form = EditSocialProfileForm(request.POST, request.FILES,
                instance=user.userprofile)
        
        if form.is_valid():
            logger.info(form.instance)
            form.save()
        if not user.userprofile.avatar:
            user.userprofile.avatar ='image/noAvatar.png'
            user.userprofile.save()
    else:    
        form = EditSocialProfileForm(instance=user.userprofile)
    args['form'] = form
    return render(request, 'user/edit_social_profile.html', args)

@login_required(login_url='/loguearse')
def edit_profile(request):
    pass


def ejecutar(request):
    context = RequestContext(request)    
    warnings = False
    if request.method == 'POST':        
        code = request.POST['code']        
        error,warnings,msg = checkCode(code)        
    return render(request, 'compile_output.html', {'error':error, 'warnings':warnings,'msg':msg})


@login_required(login_url='/loguearse')
def add_pytt(request):
    context = RequestContext(request)    
    warnings = False
    if request.method == 'POST':        
        code = request.POST['code']
        title = request.POST['title']
        error,warnings,msg = checkCode(code) 
        pytt = Pytt()
        pytt.title = title
        pytt.codigo = code
        pytt.autor = request.user
        pytt.warnings = warnings
        if error:
            pytt.funciona = False
        else:
            pytt.funciona = True
        pytt.save()
        messages.add_message(request, messages.SUCCESS, 'Se guardo tu pytt!!!')
    
    return redirect('main:home')


