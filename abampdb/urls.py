from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *
from .import views

app_name = "abampdb"
urlpatterns = [
    path('',views.IndexPage,name='index'),
    path('login/',views.LoginPage,name='login'),
    path('logout/',views.LogoutPage,name='logout'),
    path('signup/',views.SignupPage,name='signup'),
    path('enter/',views.EnterPage,name='enter'),
    path("home/", views.SearchView.as_view(), name="home"),
    path("protein/", views.ProteinView.as_view(), name="protein"),
    path("search/", views.SearchView.as_view(), name="search"),
    path("query/", views.SearchView.as_view(), name="query"),
    path("predicted/", views.PredictedView.as_view(), name="predicted"),
    path("stats/", views.StatsPage, name="stats"),
    path("about/", views.AboutUsPage, name="about_us"),
    path("tutorial/", views.TutorialPage, name="tutorial"),
    path("contact/", views.ContactView.as_view(), name="contact"),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
