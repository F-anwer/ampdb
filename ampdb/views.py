from django.shortcuts import get_object_or_404
from .models import PDBQuery, Proteins

from django import forms
from django.views import generic
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from wsgiref.util import FileWrapper

import urllib


class IndexView(generic.ListView):
    """Index first page view of the AMPdb tool"""

    model = PDBQuery
    template_name = "ampdb/index.html"
    context_object_name = "queries"


class AboutUsView(generic.ListView):
    """About Us view of the AMPdb tool"""

    model = PDBQuery
    template_name = "ampdb/about_us.html"
    context_object_name = "queries"


class ContactView(generic.ListView):
    """Contact section of the AMPdb tool."""

    model = PDBQuery
    template_name = "ampdb/contact.html"
    context_object_name = "queries"


class SearchForm(forms.Form):
    """Search view showing the top results from the main page of the AMPdb tool."""

    query_id = forms.CharField()

    def create_query(self):
        """the form fields get put into self.cleaned_data, make a new
        PDBQuery object from those fields and return"""
        query = PDBQuery(query_id=self.cleaned_data["query_id"])
        query.save()
        return query


class SearchView(generic.edit.FormView):
    """Search view of the AMPdb tool."""

    form_class = SearchForm
    template_name = "ampdb/index.html"
    success_url = "/ampdb/"

    def form_valid(self, form):
        """creates a query object and returns a redirect to the detail
        view"""
        query = form.create_query()
        return HttpResponseRedirect(
            reverse("ampdb:protein")
            + "?"
            + urllib.parse.urlencode({"name": query.query_id})
        )


class ProteinView(generic.TemplateView):
    """Protein entry view for each result with all the properties."""

    template_name = "ampdb/protein.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context["protein"] = Proteins.objects.get(
                name=self.request.GET.get("name", None)
            )
        except Proteins.DoesNotExist:
            context["protein"] = None
        return context


# class ResultsView(generic.DetailView):
#     model = PDBQuery
#     template_name = "ampdb/results.html"
#
#     def get_context_data(self, **kwargs):
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
