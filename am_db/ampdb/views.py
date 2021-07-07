from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from .models import PDBQuery

from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    return render(request, 'ampdb/index.html')

def search(request):
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)
        try:
            query = PDBQuery.objects.get(name = query_id)
            #do something with user
            html = ("<H1>%s</H1>", query)
            return HttpResponse(html)
        except PDBQuery.DoesNotExist:
            return HttpResponse("no such protein available")  
    else:
        return render(request, 'ampdb/index.html')


