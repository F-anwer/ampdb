from django.contrib import admin
from .models import PDBQuery, Proteins, Dock_Proteins, Synthetic, PDBSQuery

admin.site.register(PDBQuery)
admin.site.register(Proteins)
admin.site.register(Dock_Proteins)
admin.site.register(Synthetic)
admin.site.register(PDBSQuery)
