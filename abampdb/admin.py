from django.contrib import admin
from .models import PDBQuery, Proteins, Docks, Synthetic, PDBSQuery

admin.site.register(PDBQuery)
admin.site.register(Proteins)
admin.site.register(Docks)
admin.site.register(Synthetic)
admin.site.register(PDBSQuery)
