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
    path('recetas/new', views.add_receta, name='add_receta'),
    path('recetas/edit/<_id>', views.receta_edit, name='receta_edit'),
    path('recetas/delete/<_id>', views.recetas_delete, name='recetas_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

