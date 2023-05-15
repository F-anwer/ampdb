# forms.py
from django import forms
from .models import Proteins, Docks


class ProteinsForm(forms.ModelForm):
    class Meta:
        model = Proteins
        fields = "__all__"


class DocksForm(forms.ModelForm):
    class Meta:
        model = Docks
        fields = "__all__"
