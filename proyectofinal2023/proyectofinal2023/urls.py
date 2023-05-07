from django.contrib import admin
from django.urls import path, include
from proveedores.views import Bienvenida

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Bienvenida.as_view(), name = 'home'),
    path('proveedores/', include('proveedores.urls')),
    path('cuentas/', include('cuentas.urls')),
]
