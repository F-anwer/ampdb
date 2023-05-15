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
    path("home/", views.search_view, name="home"),
    path("protein/<proteins_id>", views.show_protein, name="protein"),
    # path("docking/", views.DockDetailView.as_view(), name="docking"),
    path("search/", views.search_view, name="search"),
    path("show_synthetic/<synthetic_id>", views.show_synthetic, name="show-synthetic"),
    path("predicted/", views.syntheticsearch, name="predicted"),
    path("stats/", views.StatsPage, name="stats"),
    path("about/", views.AboutUsPage, name="about_us"),
    path("tutorial/", views.TutorialPage, name="tutorial"),
    path("contact/", views.ContactView.as_view(), name="contact"),

    path('show_dock/<docks_id>', views.show_dock, name='show-dock'),
    
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# path("docking/", views.get_search_results, name="docking"),