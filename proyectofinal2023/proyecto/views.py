from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from .models import Proyecto
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import FormProyecto, FormProyectoEditar


class ListaProyectos(ListView):
    model = Proyecto

class NuevoProyecto(CreateView):
    model = Proyecto
    form_class = FormProyecto
    extra_context = {'accion': 'Nuevo'}
    success_url = reverse_lazy('lista_proyectos')

class EliminarProyecto(DeleteView):
    model = Proyecto
    success_url = reverse_lazy('lista_proyectos') 
    
def eliminar_todos(request):
    if request.method == 'POST':
        for id in request.POST:
            if id == "csrfmiddlewaretoken":
                continue
            elif id == "todos":
                Proyecto.objects.all().delete()
                return redirect('lista_proyectos')
            Proyecto.objects.get(id=id).delete()
    
    return redirect('lista_proyectos')

class EditarProyecto(UpdateView):
    model = Proyecto
    form_class = FormProyectoEditar
    extra_context = {'accion': 'Editar'}
    success_url = reverse_lazy('lista_proyectos')

