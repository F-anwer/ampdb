from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = "abampdb"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("abampdb/login/", views.LoginInView.as_view(), name="login"),
    path("home/", views.SearchView.as_view(), name="home"),
    path("protein/", views.ProteinView.as_view(), name="protein"),
    path("search/", views.SearchView.as_view(), name="search"),
    path("query/", views.SearchView.as_view(), name="query"),
    path("stats/", views.StatsView.as_view(), name="stats"),
    path("about/", views.AboutUsView.as_view(), name="about_us"),
    path("tutorial/", views.TutorialView.as_view(), name="tutorial"),
    path("contact/", views.ContactView.as_view(), name="contact"),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
