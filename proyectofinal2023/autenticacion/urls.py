from django.urls import path
from .views import VRegistro,cerrarSesion, loguear

urlpatterns = [
    path('', VRegistro.as_view(), name = "Autenticacion"),
    path('cerrar_sesion', cerrarSesion, name = "cerrar_sesion"),
    path('iniciar_sesion', loguear, name = "iniciar_sesion"),

]