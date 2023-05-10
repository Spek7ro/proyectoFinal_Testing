from django.urls import path
from .views import VRegistro,cerrarSesion, loguear,reestablecer_contraseña

urlpatterns = [
    path('', VRegistro.as_view(), name = "Autenticacion"),
    path('cerrar_sesion', cerrarSesion, name = "cerrar_sesion"),
    path('iniciar_sesion', loguear, name = "iniciar_sesion"),
    path('reestablecer_contraseña', reestablecer_contraseña, name = "reestablecer_contra"),

]