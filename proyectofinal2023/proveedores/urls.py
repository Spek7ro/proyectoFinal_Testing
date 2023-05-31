from django.urls import path, include
from proveedores import views

urlpatterns = [
    path('', views.ListaProveedores.as_view(), name = 'lista_proveedores'),
    path('agregar/', views.NuevoProveedor.as_view(), name = 'agregar_proveedor'),
    path('editar/<int:pk>', views.EditarProveedor.as_view(), name = 'editar_proveedor'),
    path('eliminar/<int:pk>', views.EliminarProveedor.as_view(), name = 'eliminar_proveedor'),
    path('eliminar-proveedores', views.eliminar_proveedores, name = 'eliminar_proveedores'),
    path('pdf/', views.generar_reporte, name='reporte_proveedores'),
]