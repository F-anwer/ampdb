
import contextlib
from django.template import loader
import urllib
# from wsgiref.util import FileWrapper
from django import forms
import itertools
# from django.http import HttpResponse, HttpResponseRedirect
# from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import *

from .models import PDBQuery, Proteins, Docks, PDBDQuery, Synthetic
import uuid
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings
import os
from django.views.generic import ListView
from django.db.models import Q

from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.views.generic.edit import FormView



def EnterPage(request):
    return render(request, "abampdb/search.html")


def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('/login/')
    return render(request, 'abampdb/signup.html')

def LoginPage(request):

    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('/search/')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")
    return render (request,'abampdb/login.html')

def LogoutPage(request):
    logout(request)
    return redirect('/login/')


def IndexPage(request):
    return render(request, "abampdb/index.html") 

   
def AboutUsPage(request):
    return render(request, "abampdb/about_us.html")  

   
def StatsPage(request):
    return render(request, "abampdb/stats.html")  



class ContactView(generic.TemplateView):
    """Contact section of the AMPdb tool."""

    model = PDBQuery
    template_name = "abampdb/contact.html"


def TutorialPage(request):
    return render(request, "abampdb/tutorial.html")

def show_protein(request, proteins_id):
    protein = Proteins.objects.get(pk=proteins_id)
    return render(request, 'abampdb/protein.html', {'protein': protein})


def search_view(request):

    protein_list = Proteins.objects.all()
    dock_list = Docks.objects.all()
    return render(request, 'abampdb/search.html', {'protein_list': protein_list, 'dock_list': dock_list,})
       


def show_dock(request, docks_id):
    dock = Docks.objects.get(pk=docks_id)
    return render(request, 'abampdb/docking.html', {'dock': dock})


def show_synthetic(request, synthetic_id):
    synthetic = Synthetic.objects.get(pk=synthetic_id)
    return render(request, 'abampdb/synthetic.html', {'synthetic': synthetic})

def syntheticsearch(request):

    synthetic_list = Synthetic.objects.all()
    return render(request, 'abampdb/predicted.html', {'synthetic_list': synthetic_list})


  

