from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from .models import Proyecto
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import FormProyecto, FormProyectoEditar, FiltrosProyecto
from django.core.paginator import Paginator


class ListaProyectos(ListView):
    model = Proyecto
    paginate_by = 5
    extra_context = {'form':FiltrosProyecto}

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

def buscar_proyecto(request):
    proyecto = Proyecto.objects.all().order_by('num_proyecto','nombre_proyecto')
    
    if request.method == 'POST':
        
        form = FiltrosProyecto(request.POST)
        num_proyecto = request.POST.get('num_proyecto',None)
        nombre_proyecto = request.POST.get('nombre_proyecto',None)
        objetivo = request.POST.get('objetivo',None)
        presupuesto = request.POST.get('presupuesto',None)
        duracion = request.POST.get('duracion',None)
        responsables = request.POST.get('responsables',None)
        proveedor = request.POST.get('proveedor',None)
        
        if num_proyecto:
            # proyecto = proyecto.filter(num_proyecto__startswith=num_proyecto)
            proyecto = proyecto.filter(num_proyecto__contains=num_proyecto)
            proyecto = proyecto.filter(num_proyecto__icontains=num_proyecto)
            # proyecto = proyecto.get(num_proyecto=num_proyecto)
        if nombre_proyecto:
            proyecto = proyecto.filter(nombre_proyecto=nombre_proyecto)
        if objetivo:
            proyecto = proyecto.filter(objetivo=objetivo)
        if presupuesto:
            proyecto = proyecto.filter(presupuesto=presupuesto)
        if duracion:
            proyecto = proyecto.filter(duracion=duracion)
        if responsables:
            proyecto = proyecto.filter(responsables=responsables)
        if proveedor:
            proyecto = proyecto.filter(proveedor=proveedor)
        
            
    else:
        form = FiltrosProyecto()
        
    paginator = Paginator(proyecto, 2)  # Show 25 contacts per page.
    page_number = request.POST.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'object_list': page_obj,
        'page_obj': page_obj,
        'form': form
    } 
    return render(request, 'proyecto/proyecto_list.html', context)