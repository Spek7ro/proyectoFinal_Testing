from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Proveedor, Municipio, Estado
from .forms import FormProveedor, FormProveedorEditar, FiltrosProveedor
from django.http import JsonResponse
from django.core.paginator import Paginator

class ListaProveedores(ListView):
    model = Proveedor
    paginate_by = 5
    extra_context = {'form': FiltrosProveedor}
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

def buscar_proveedor(request):
    proveedor = Proveedor.objects.all().order_by('rfc','estado')
    
    if request.method == 'POST':
        
        form = FiltrosProveedor(request.POST)
        rfc = request.POST.get('rfc',None)
        razon_social = request.POST.get('razon_social',None)
        direccion = request.POST.get('direccion',None)
        telefono = request.POST.get('telefono',None)
        correo = request.POST.get('correo',None)
        estado = request.POST.get('estado',None)
        municipio = request.POST.get('municipio',None)
        
        if rfc:
            # proveedor = proveedor.filter(rfc__startswith=rfc)
            proveedor = proveedor.filter(rfc__contains=rfc)
            proveedor = proveedor.filter(rfc__icontains=rfc)
            # proveedor = proveedor.get(rfc=rfc)
        if razon_social:
            proveedor = proveedor.filter(razon_social=razon_social)
        if direccion:
            proveedor = proveedor.filter(direccion=direccion)
        if telefono:
            proveedor = proveedor.filter(telefono=telefono)
        if correo:
            proveedor = proveedor.filter(correo=correo)
        if estado:
            proveedor = proveedor.filter(estado=estado)
        if municipio:
            proveedor = proveedor.filter(municipio=municipio)
            
    else:
        form = FiltrosProveedor()
        
    paginator = Paginator(proveedor, 2)  # Show 25 contacts per page.
    page_number = request.POST.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'object_list': page_obj,
        'page_obj': page_obj,
        'form': form
    } 
    return render(request, 'proveedores/proveedor_list.html', context)