from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('hola/', hola_mundo, name="hola_mundo"),
    path('', lista_contactos, name= 'lista_contactos'),
    path('agregar', agregar_contactos, name='agregar_contactos'),
    path('editar/<int:id>', editar_contacto, name='editar_contacto'),
    path('eliminar/<int:id>', eliminar_contacto, name='eliminar_contacto'),
    path('editar/<int:id>/', editar_contacto, name='editar_contacto'),
    path('crear/', crear_usuario, name='crear_usuario'),
    path('loguear/', logeo.as_view(), name='loguear')
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)