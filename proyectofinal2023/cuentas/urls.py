from django.urls import path, include
from cuentas import views

urlpatterns = [
    path('', views.ListaCuentasBancarias.as_view(), name = 'lista_cuentas'),
    path('agregar/', views.NuevaCuentaBancaria.as_view(), name = 'agregar_cuenta'),
    path('editar/<int:pk>', views.EditarCuentaBancaria.as_view(), name = 'editar_cuenta'),
    path('eliminar/<int:pk>', views.EliminarCuentaBancaria.as_view(), name = 'eliminar_cuenta'),
    path('eliminar-materias', views.eliminar_todas, name = 'eliminar_todas'),
    path('buscar-cuenta', views.buscar_cuenta, name='buscar_cuenta'),
    
    #path('buscar/', views.Buscarcuenta, name = 'buscar_cuenta'),
]