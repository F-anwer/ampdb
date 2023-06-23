from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import PDBQuery, Proteins, Docks, Targetproteins, Video

admin.site.register(PDBQuery)
admin.site.register(Proteins)
admin.site.register(Docks)
class VideoAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Video)

