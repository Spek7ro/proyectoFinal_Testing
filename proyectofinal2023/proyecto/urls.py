from django.urls import path, include
from proyecto import views

urlpatterns = [
    path('', views.ListaProyectos.as_view(), name = 'lista_proyectos'),
    path('agregar/', views.NuevoProyecto.as_view(), name = 'agregar_proyecto'),
    path('editar/<int:pk>', views.EditarProyecto.as_view(), name = 'editar_proyecto'),
    path('eliminar/<int:pk>', views.EliminarProyecto.as_view(), name = 'eliminar_proyecto'),
    path('eliminar-proyectos', views.eliminar_todos, name = 'eliminar_todos'),
    path('buscar-proyecto', views.buscar_proyecto, name = 'buscar_proyectos'),
]