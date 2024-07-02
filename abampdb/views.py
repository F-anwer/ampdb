
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

from .models import PDBQuery, Proteins, Docks, PDBDQuery, Targetproteins
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
from abampdb.forms import SearchForm
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

    return render(request, 'abampdb/tutorial.html')

def search_view(request):
    return render(request, "abampdb/search.html", {
        "targets": Targetproteins.objects.all(),
        "proteins": Proteins.objects.all()
    })

def protein(request, proteins_id):
    protein = Proteins.objects.get(pk=proteins_id)
    target_protien = protein.target_protein.id
    protein_name = protein.amp[2:]
    dock = Docks.objects.filter(Q(targets=target_protien) &  Q(dock_1__icontains=f"_{protein_name}.pdb"))

    
    # dock_id = dock[0].id
    # protein_data= Proteins.objects.get(dock=dock_id)
    
    return render(request, "abampdb/protein.html", {
        "protein": protein,
        "dock": dock,
    })

def target_proteins(request, proteins_id):
    protein = get_object_or_404(Proteins, pk=proteins_id)

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            amp = form.cleaned_data['amp']
            target_proteins = form.cleaned_data['target_proteins']
            docks = Docks.objects.filter(targets__in=target_proteins, proteins=amp)
            # Do something with the filtered docks
    else:
        form = SearchForm()
    return render(request, 'search.html', {'form': form})

def create_protien(request):
    if request.method == 'POST':
        protein_id = request.POST.get('protein_id')
        protein_name = request.POST.get('protein_name')
        score = request.POST.get('score')
        sequence = request.POST.get('sequence')
        target_protein_id = request.POST.get('target_id')
        
        # Retrieve other form data in a similar manner
        if not target_protein_id:
            # Re-render the form with an error message
            return redirect(reverse('abampdb:search'))
        
        try:
            protien = Proteins.objects.get(id=protein_id)
            protien.target_protein_id = target_protein_id
            protien.save()
            target_protein = Targetproteins.objects.get(id=target_protein_id)
            target_protein_name  = target_protein.targets + '_' + protien.pdb_name[2:]
            docks_instances = Docks.objects.filter(dock_1__contains=target_protein_name)
            for dock_instance in docks_instances:
                dock_instance.targets.add(target_protein)
                
            redirect_url = reverse('abampdb:protein', kwargs={'proteins_id': protein_id})
            return redirect(redirect_url)
        except Proteins.DoesNotExist:
            return HttpResponse('Protein not found')
        
    else:
            return HttpResponse('Invalid request method')





  

