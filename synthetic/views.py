from django.shortcuts import render
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
from django.contrib.auth import authenticate, login, logout
from .models import *

from .models import Synthetic, Sdock, PDBSDQuery, Stargetproteins
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

# Create your views here.


def synthetic(request):
    return render(request, "synthetic/predicted.html", {
        "starget": Stargetproteins.objects.all(),
        "synthetic": Synthetic.objects.all()
    })


def submit_synthetic(request, synthetic_id):
    synthetic = Synthetic.objects.get(pk=synthetic_id)

    starget_protein = synthetic.starget_protein.id
    print("starget_protein", starget_protein)
    sdock = Sdock.objects.filter(Q(stargets=starget_protein))
    sdock2 = Sdock.objects.filter(Q(s_dock__icontains=synthetic.name))

    # synthetic_title = synthetic.title[2:]
    # sdock = Sdock.objects.filter(Q(stargets=starget_protein) & Q(
    #     s_dock__icontains=f"_{synthetic_title}.pdb"))

    print("sdock", sdock)
    print("sdock2", sdock2)

    # dock_id = dock[0].id
    # protein_data= Proteins.objects.get(dock=dock_id)

    return render(request, "synthetic/synthetic.html", {
        "synthetic": synthetic,
        "sdock": sdock,
    })


# def synthetic_targets(request, synthetic_id):
#     synthetic = get_object_or_404(Synthetic, pk=synthetic_id)

#     if request.method == 'POST':
#         form = PSearchForm(request.POST)
#         if form.is_valid():
#             synthetic = form.cleaned_data['synthetic']
#             synthetic_targets = form.cleaned_data['synthetic_targets']
#             sdocks = Sdock.objects.filter(
#                 stargets__in=synthetic_targets, synthetic=synthetic)
#             # Do something with the filtered docks
#     else:
#         form = PSearchForm()
#     return render(request, 'predicted.html', {'form': form})


def create_syntheticprotien(request):
    if request.method == 'POST':
        synthetic_id = request.POST.get('synthetic_id')
        print(synthetic_id)
        starget_protein_id = request.POST.get('starget_id')

        # Retrieve other form data in a similar manner

        try:
            synthetic = Synthetic.objects.get(id=synthetic_id)
            synthetic.starget_protein_id = starget_protein_id
            synthetic.save()
            redirect_url = reverse('synthetic:submit_synthetic', kwargs={
                                   'synthetic_id': synthetic_id})
            return redirect(redirect_url)
        except Synthetic.DoesNotExist:
            return HttpResponse('Protein not found')

    else:
        return HttpResponse('Invalid request method')
