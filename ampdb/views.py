import urllib
from wsgiref.util import FileWrapper

from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic
import itertools

from .models import PDBQuery, Proteins


class IndexView(generic.TemplateView):
    """Index first page view of the AMPdb tool"""

    template_name = "ampdb/index.html"


class LoginInView(generic.TemplateView):
    """Index first page view of the AMPdb tool"""

    template_name = "ampdb/login.html"


class AboutUsView(generic.TemplateView):
    """About Us view of the AMPdb tool"""

    template_name = "ampdb/about_us.html"


class StatsView(generic.TemplateView):
    """About Us view of the AMPdb tool"""

    template_name = "ampdb/stats.html"


class ContactView(generic.TemplateView):
    """Contact section of the AMPdb tool."""

    model = PDBQuery
    template_name = "ampdb/contact.html"
    context_object_name = "queries"


class TutorialView(generic.TemplateView):
    """Contact section of the AMPdb tool."""

    template_name = "ampdb/tutorial.html"


class SearchForm(forms.Form):
    """Search view showing the top results from the main page of the AMPdb tool."""

    query_id = forms.CharField()
    pdb_name = forms.CharField()
    target_protein = forms.CharField()

    def create_query(self):
        """the form fields get put into self.cleaned_data, make a new
        PDBQuery object from those fields and return"""
        query = Proteins(name=self.cleaned_data["pdb_name"])
        query.save()
        return query


class SearchView(generic.FormView):
    """Search view of the AMPdb tool."""

    template_name = "ampdb/search.html"

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        rows = []

        target_proteins = [
            'Omp38',
            'OmpW',
            'OmpA',
            'Omp33-36',
            'Oxa51like',
        ]

        for protein, name in itertools.zip_longest(Proteins.objects.all(), target_proteins):
            rows.append({
                'left': protein,
                'right': name,
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
            reverse("ampdb:protein")
            + "?"
            + urllib.parse.urlencode({
                "pdb_name": form['pdb_name'].value(),
                "target_protein": form['target_protein'].value()}))


class ProteinView(generic.TemplateView):
    """Protein entry view for each result with all the properties."""

    template_name = "ampdb/protein.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context["protein"] = Proteins.objects.get(
                name=self.request.GET.get("pdb_name", None)
            )
        except Proteins.DoesNotExist:
            context["protein"] = None
        return context

# class ResultsView(generic.DetailView):
#     model = PDBQuery
#     template_name = "ampdb/results.html"
#
#     def get_context_data(self, **kwargs):  e
#         context = super().get_context_data(**kwargs)
#         try:
#             context["protein"] = Proteins.objects.get(
#                 name=self.request.GET.get("name", None)
#             )
#         except Proteins.DoesNotExist:
#             context["protein"] = None
#
#         return context

# def search(self):
#     if request.method == 'GET':
#     try:
#         query = PDBQuery.objects.get(name = query_id)
#         if query_id == search_id:
#             return get_object_or_404(html)
#     except PDBQuery.DoesNotExist:
#         return HttpResponse("no such protein available")
# else:
#     return render(request, 'ampdb/index.html')
