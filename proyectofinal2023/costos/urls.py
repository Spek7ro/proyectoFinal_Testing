from django.urls import path, include
from costos import views

urlpatterns = [
    path('', views.ListaCostos.as_view(), name = 'lista_costos'),
    path('agregar/', views.NuevoCosto.as_view(), name = 'agregar_costo'),
    path('editar/<int:pk>', views.EditarCosto.as_view(), name = 'editar_costo'),
    path('eliminar/<int:pk>', views.EliminarCosto.as_view(), name = 'eliminar_costo'),
    path('eliminar-costos', views.eliminar_costos, name = 'eliminar_costos'),
]