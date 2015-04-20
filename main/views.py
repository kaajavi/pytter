# -*- encoding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.template.defaulttags import NowNode
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.decorators import login_required

##Errores
from django.http import Http404

##BASE DE DATOS
from django.db.models import Q
##MENSAJES A LA VISTA (Cuadros de alertas, info, warning, etc
from django.contrib import messages

##TIEMPOS
from datetime import date

# Create your views here.
def home (request):
    context = RequestContext(request)
    return render_to_response('base.html', 
                              {}, 
                              context)

def ejecutar(request):
    context = RequestContext(request)
    print "LLLLEEEEGGGAAAA"
    
    
    print "LLLLEEEEGGGAAAA"

    return HttpResponse("HOOLAAA") 
