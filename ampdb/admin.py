from django.contrib import admin
from .models import PDBQuery, Proteins

admin.site.register(PDBQuery)
admin.site.register(Proteins)
