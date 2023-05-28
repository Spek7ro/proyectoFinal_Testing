from django.contrib import admin
from django.urls import path, include
from proveedores.views import Bienvenida

from autenticacion.views import loguear

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loguear, name = 'iniciar_sesion'),
    path('bienvenida', Bienvenida.as_view(), name = 'home'),
    path('proveedores/', include('proveedores.urls')),
    path('autenticacion/', include('autenticacion.urls')),
    path('cuentas/', include('cuentas.urls')),
    path('proyectos/', include('proyecto.urls')),
    path('costos/', include('costos.urls')),
]
