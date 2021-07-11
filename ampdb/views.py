from django.shortcuts import get_object_or_404
from .models import PDBQuery, Proteins

from django import forms
from django.views import generic
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect


class IndexView(generic.ListView):
    model = PDBQuery
    template_name = 'ampdb/index.html'
    context_object_name = 'queries'

    # def get_queryset(self):
    #     return PDBQuery.objects.all()


class SearchForm(forms.Form):
    query_id = forms.CharField()

    def create_query(self):
        """ the form fields get put into self.cleaned_data, make a new
        PDBQuery object from those fields and return """
        query = PDBQuery(query_id=self.cleaned_data['query_id'])
        query.save()
        return query


class SearchView(generic.edit.FormView):
    form_class = SearchForm
    template_name = 'search.html'
    success_url = '/ampdb/'

    def form_valid(self, form):
        """ creates a query object and returns a redirect to the detail
        view """
        query = form.create_query()
        return HttpResponseRedirect(reverse('ampdb:results', args=(query.id,)))


class ResultsView(generic.DetailView):
    model = PDBQuery
    template_name = 'ampdb/results.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['system'] = self.request.GET.get('system', None)
        try:
            context['protein'] = Proteins.objects.get(
                    name=self.object.query_id)
        except Proteins.DoesNotExist:
            context['protein'] = None

        return context

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
