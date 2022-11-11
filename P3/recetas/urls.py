# recetas/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('busqueda', views.busqueda, name='busqueda'),
    path('detalle/<_id>', views.detalle, name='detalle'),
    path('darkmode', views.darkmode, name='darkmode'),
    path('recetas', views.recetas, name='recetas')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

