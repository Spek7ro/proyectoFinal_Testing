from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import CuentaBancaria
from django.core.paginator import Paginator
from .forms import FormCuentaBancaria, FormCuentaBancariaEditar, FiltrosCuenta


class ListaCuentasBancarias(ListView):
    paginate_by = 5
    model = CuentaBancaria
    extra_context = {'form': FiltrosCuenta}

class NuevaCuentaBancaria(CreateView):
    model = CuentaBancaria
    form_class = FormCuentaBancaria
    extra_context = {'accion': 'Nueva'}
    success_url = reverse_lazy('lista_cuentas')

class EliminarCuentaBancaria(DeleteView):
    model = CuentaBancaria
    success_url = reverse_lazy('lista_cuentas') 
    
def eliminar_todas(request):
    if request.method == 'POST':
        for id in request.POST:
            if id == "csrfmiddlewaretoken":
                continue
            elif id == "todas":
                CuentaBancaria.objects.all().delete()
                return redirect('lista_cuentas')
            CuentaBancaria.objects.get(id=id).delete()
    
    return redirect('lista_cuentas')

class EditarCuentaBancaria(UpdateView):
    model = CuentaBancaria
    form_class = FormCuentaBancariaEditar
    extra_context = {'accion': 'Editar'}
    success_url = reverse_lazy('lista_cuentas')

class Bienvenida(TemplateView):
    template_name = 'home.html'

def buscar_cuenta(request):
    cuentas = CuentaBancaria.objects.all().order_by('idcuenta','responsable')
    
    if request.method == 'POST':
        
        form = FiltrosCuenta(request.POST)
        idcuenta = request.POST.get('idcuenta',None)
        proyecto = request.POST.get('proyecto',None)
        responsable = request.POST.get('responsable',None)
        limite_presupuestario = request.POST.get('limite_presupuestario',None)
        if idcuenta:
            cuentas = cuentas.filter(idcuenta__contains=idcuenta)
        if proyecto:
            # cuentas = cuentas.filter(proyecto__startswith=proyecto)
            #cuentas = cuentas.filter(proyecto__contains=proyecto)
            #cuentas = cuentas.filter(proyecto__icontains=proyecto)
            cuentas = cuentas.get(proyecto__contains=proyecto)
        if responsable:
            cuentas = cuentas.filter(responsable__contains=responsable)
        if limite_presupuestario:
            cuentas = cuentas.filter(limite_presupuestario__contains=limite_presupuestario)
        
            
        print(cuentas.query)
            
    else:
        form = FiltrosCuenta()
        
    paginator = Paginator(cuentas, 2)  # Show 25 contacts per page.
    page_number = request.POST.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'object_list': page_obj,
        'page_obj': page_obj,
        'form': form
    } 
    return render(request, 'cuentas/cuentabancaria_list.html', context)