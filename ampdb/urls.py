from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'ampdb'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),

]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

