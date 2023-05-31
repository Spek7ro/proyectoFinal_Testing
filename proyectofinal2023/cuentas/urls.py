from django.urls import path, include
from cuentas import views

urlpatterns = [
    path('', views.ListaCuentasBancarias.as_view(), name = 'lista_cuentas'),
    path('agregar/', views.NuevaCuentaBancaria.as_view(), name = 'agregar_cuenta'),
    path('editar/<int:pk>', views.EditarCuentaBancaria.as_view(), name = 'editar_cuenta'),
    path('eliminar/<int:pk>', views.EliminarCuentaBancaria.as_view(), name = 'eliminar_cuenta'),
    path('eliminar-cuentas', views.eliminar_cuentas, name = 'eliminar_cuentas'),
    path('pdf/', views.generar_reporte, name='reporte_cuentas'),

    #path('buscar/', views.Buscarcuenta, name = 'buscar_cuenta'),
]