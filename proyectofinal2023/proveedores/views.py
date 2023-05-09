from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Proveedor, Municipio, Estado
from .forms import FormProveedor, FormProveedorEditar
from django.http import JsonResponse
from django.core.paginator import Paginator

class ListaProveedores(ListView):
    model = Proveedor

class NuevoProveedor(CreateView):
    model = Proveedor
    form_class = FormProveedor
    extra_context = {'accion': 'Nuevo'}
    success_url = reverse_lazy('lista_proveedores')

class EliminarProveedor(DeleteView):
    model = Proveedor
    success_url = reverse_lazy('lista_proveedores') 
    
def eliminar_todos(request):
    if request.method == 'POST':
        for id in request.POST:
            if id == "csrfmiddlewaretoken":
                continue
            elif id == "todas":
                Proveedor.objects.all().delete()
                return redirect('lista_proveedores')
            Proveedor.objects.get(id=id).delete()
    
    return redirect('lista_proveedores')

class EditarProveedor(UpdateView):
    model = Proveedor
    form_class = FormProveedorEditar
    extra_context = {'accion': 'Editar'}
    success_url = reverse_lazy('lista_proveedores')

class Bienvenida(TemplateView):
    template_name = 'home.html'

def buscar_municipios(request):
    id_estado = request.POST.get('id_estado', None)
    if id_estado:
        municipios = Municipio.objects.filter(estado_id = id_estado)
        data = [{'id':mun.id, 'nombre':mun.nombre} for mun in municipios]
        return JsonResponse(data, safe=False)
    return JsonResponse({'error':'Parametro Invalido'}, safe=False)