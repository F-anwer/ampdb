from django.contrib import admin
from .models import Synthetic, PDBSQuery, Stargetproteins, Sdock, PDBSTQuery

# Register your models here.
admin.site.register(Synthetic)
admin.site.register(PDBSQuery)
admin.site.register(Stargetproteins)
admin.site.register(Sdock)