from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "ampdb"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("protein/", views.ProteinView.as_view(), name="protein"),
    path("search/", views.SearchView.as_view(), name="search"),
    path("about/", views.AboutUsView.as_view(), name="about_us"),
    path("tutorial/", views.TutorialView.as_view(), name="tutorial"),
    path("contact/", views.ContactView.as_view(), name="contact"),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
