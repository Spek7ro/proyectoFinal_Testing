from django.urls import path, include
from .views import VRegistro,cerrarSesion

urlpatterns = [
    path('', VRegistro.as_view(), name = "Autenticacion"),
    path('cerrar_sesion', cerrarSesion, name = "cerrar_sesion"),

]