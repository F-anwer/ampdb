import urllib
# from wsgiref.util import FileWrapper

from django import forms
# from django.http import HttpResponse, HttpResponseRedirect
# from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic
import itertools
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import *

from .models import PDBQuery, Proteins, Dock_Proteins
import uuid
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings
import os

@login_required(login_url='/login/')
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

@login_required(login_url='/login/')
def IndexPage(request):
    return render(request, "abampdb/index.html") 

@login_required(login_url='/login/')   
def AboutUsPage(request):
    return render(request, "abampdb/about_us.html")  

@login_required(login_url='/login/')   
def StatsPage(request):
    return render(request, "abampdb/stats.html")  



class ContactView(generic.TemplateView):
    """Contact section of the AMPdb tool."""

    model = PDBQuery
    template_name = "abampdb/contact.html"


def TutorialPage(request):
    return render(request, "abampdb/tutorial.html")

class PredictedForm(forms.Form):
    """Search view showing the top results from the main page of the AMPdb tool."""

    # query_id = forms.CharField()
    synthetic_pdb_name = forms.CharField()
    
    def create_query(self):
        """the form fields get put into self.cleaned_data, make a new
        PDBQuery object from those fields and return"""
        query = Synthetic(name=self.cleaned_data["synthetic_pdb_name"])
        query.save()
        return query


class PredictedView(generic.TemplateView):
    """About Us view of the AMPdb tool"""  
    form_class = PredictedForm
    template_name = "abampdb/predicted.html"
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super(PredictedView, self).get_context_data(**kwargs)
        rows = []

        target_proteins = ['Omp38',
            'OmpW',
            'OmpA',
            'Omp33-36',
            'Oxa51like',
            'oprD',
            'cat1',
            'cm1A',
            'FBN',
            'fic',
            'fimH',
            'gentamicin',
            'IMP',
            'LptD',
            'Oxa-51 like M',
            'adeA',
            'adeC',
            'adeR',
            'adeS',
            'ampC',
            'baeR',
            'baeS',
            'bfmR',
            'bfmS',
            'blaOXA-33',
            'cpaA',
            'gacA',
            'gacS',
            'intl1',
            'smpA',
        ]

        for peptide, protein in itertools.zip_longest(Synthetic.objects.all(), target_proteins):
            rows.append({
                'left': peptide,
                'right': protein,
            })
        context['rows'] = rows

        context['name'] = Synthetic.objects.all()
        try:
            context["name"] = Synthetic.objects.get(
                name=self.request.GET.getlist("synthetic_pdb_name")
            )
        except Synthetic.DoesNotExist:
            context["name"] = None
        return context

    def form_valid(self, form):
        """creates a query object and returns a redirect to the detail
        view"""

        return HttpResponseRedirect(
            reverse("ampdb:predicted")
            + "?"
            + urllib.parse.urlencode({
                "synthetic_pdb_name": form['synthetic_pdb_name'].value()}))


class SearchForm(forms.Form):
    """Search view showing the top results from the main page of the AMPdb tool."""

    # query_id = forms.CharField()
    pdb_name = forms.CharField()
    
    def create_query(self):
        """the form fields get put into self.cleaned_data, make a new
        PDBQuery object from those fields and return"""
        query = Proteins(name=self.cleaned_data["pdb_name"])
        query.save()
        return query



class SearchView(generic.FormView):
    """Search view of the AMPdb tool."""
    form_class = SearchForm
    template_name = "abampdb/search.html"
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        rows = []
        # proteinpdbs = Dock_Proteins.objects.get( pdb_name=self.request.GET.getlist("pdb_name") )
       # for pdb in proteinpdbs:
      #      print(pdb)
# docks = Dock_Proteins.objects.get( name=self.request.GET.getlist("dock_1") )

        target_proteins = [
            'Omp38',
            'OmpW',
            'OmpA',
            'Omp33-36',
            'Oxa51like',
            'oprD',
            'cat1',
            'cm1A',
            'FBN',
            'fic',
            'fimH',
            'gentamicin',
            'IMP',
            'LptD',
            'Oxa-51 like M',
            'adeA',
            'adeC',
            'adeR',
            'adeS',
            'ampC',
            'baeR',
            'baeS',
            'bfmR',
            'bfmS',
            'blaOXA-33',
            'cpaA',
            'gacA',
            'gacS',
            'intl1',
            'smpA',
        ]

        for peptide, protein in itertools.zip_longest(Proteins.objects.all(), target_proteins):
            rows.append({
                'left': peptide,
                'right': protein,
            })
        context['rows'] = rows

        context['proteins'] = Proteins.objects.all()
        try:
            context["protein"] = Proteins.objects.get(
                name=self.request.GET.getlist("pdb_name")
            )
        except Proteins.DoesNotExist:
            context["protein"] = None
        return context

    def form_valid(self, form):
        """creates a query object and returns a redirect to the detail
        view"""

        return HttpResponseRedirect(
            reverse("abampdb:protein")
            + "?"
            + urllib.parse.urlencode({
                "pdb_name": form['pdb_name'].value()}))


class ProteinView(generic.TemplateView):
    """Protein entry view for each result with all the properties."""

    template_name = "abampdb/protein.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context["protein"] = Proteins.objects.get(
                name=self.request.GET.get("pdb_name", None)
            )
        except Proteins.DoesNotExist:
            context["protein"] = None
        return context
