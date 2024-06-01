from django.urls import path
from .views import VRegistro, cerrarSesion, loguear
from .views import reestablecer_contraseña, error404

urlpatterns = [
    path('', VRegistro.as_view(), name="Autenticacion"),
    path('cerrar_sesion', cerrarSesion, name="cerrar_sesion"),
    path('iniciar_sesion', loguear, name="iniciar_sesion"),
    path('reestablecer_contraseña', reestablecer_contraseña,
         name="reestablecer_contra"),
    path('error_404', error404, name="error_404"),
]
