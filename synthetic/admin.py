from django.contrib import admin
from .models import Synthetic, PDBSQuery

# Register your models here.
admin.site.register(Synthetic)
admin.site.register(PDBSQuery)