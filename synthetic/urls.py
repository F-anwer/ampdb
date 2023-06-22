from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *
from .import views

app_name = "synthetic"
urlpatterns = [
    path('synthetic/', views.synthetic, name='synthetic'),
    path('create_syntheticprotien/', views.create_syntheticprotien,
         name='create_syntheticprotien'),
    path("synthetic/<int:synthetic_id>", views.submit_synthetic, name='submit_synthetic'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

