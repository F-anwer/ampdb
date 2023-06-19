from django.contrib import admin
from .models import PDBQuery, Proteins, Docks, Synthetic, PDBSQuery, Targetproteins, Stargetproteins, Sdock, PDBSTQuery

admin.site.register(PDBQuery)
admin.site.register(Proteins)
admin.site.register(Docks)
admin.site.register(Synthetic)
admin.site.register(PDBSQuery)
admin.site.register(Targetproteins)
admin.site.register(Stargetproteins)
admin.site.register(Sdock)
