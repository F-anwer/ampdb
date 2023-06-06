# forms.py
from django import forms
from .models import Proteins, Targetproteins

class SearchForm(forms.Form):
    amp = forms.ModelChoiceField(queryset=Proteins.objects.all())
    target_proteins = forms.ModelMultipleChoiceField(queryset=Targetproteins.objects.all())