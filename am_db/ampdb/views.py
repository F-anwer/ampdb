from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from .models import PDBQuery

from django.views import generic
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect



class IndexView(generic.ListView):
    template_name = 'ampdb/index.html'

    def get_queryset(self):
        pass
    
        # def search(self, request):
    #     if request.method == 'GET':
    #         search_id = request.GET.get('textfield', None)
    #         try:
    #             query = PDBQuery.objects.get(name = query_id)
    #             html = ("<H1>%s</H1>", query)
    #             return HttpResponse(html)
    #         except PDBQuery.DoesNotExist:
    #             return HttpResponse("no such protein available")  
    #     else:
    #         return render(request, 'ampdb/index.html')



class ResultsView(generic.DetailView):
    model = PDBQuery
    template_name = 'ampdb/results.html'
    context_object_name = 'query_id'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['book_list'] = PDBQuery.objects.all()
        return context