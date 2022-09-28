import urllib
# from wsgiref.util import FileWrapper

from django import forms
# from django.http import HttpResponse, HttpResponseRedirect
# from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic
import itertools
from django.http import HttpResponseRedirect

from .models import PDBQuery, Proteins, Dock_Proteins


class IndexView(generic.TemplateView):
    """Index first page view of the AMPdb tool"""

    template_name = "abampdb/index.html"


class LoginInView(generic.TemplateView):
    """Index first page view of the AMPdb tool"""

    template_name = "abampdb/login.html"


class AboutUsView(generic.TemplateView):
    """About Us view of the AMPdb tool"""

    template_name = "abampdb/about_us.html"


class StatsView(generic.TemplateView):
    """About Us view of the AMPdb tool"""

    template_name = "abampdb/stats.html"


class ContactView(generic.TemplateView):
    """Contact section of the AMPdb tool."""

    model = PDBQuery
    template_name = "abampdb/contact.html"


class TutorialView(generic.TemplateView):
    """Contact section of the AMPdb tool."""

    template_name = "abampdb/tutorial.html"


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
    success_url = "/abampdb"

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

