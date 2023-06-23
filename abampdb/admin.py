from django.contrib import admin
from .models import PDBQuery, Proteins, Docks, Targetproteins

admin.site.register(PDBQuery)
admin.site.register(Proteins)
admin.site.register(Docks)


