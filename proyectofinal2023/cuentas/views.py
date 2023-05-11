from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import CuentaBancaria
from .forms import FormCuentaBancaria, FormCuentaBancariaEditar
from django.contrib.auth.mixins import LoginRequiredMixin
from proyectofinal2023.utils import StaffRequiredMixin


class ListaCuentasBancarias(LoginRequiredMixin,ListView):
    model = CuentaBancaria

class NuevaCuentaBancaria(StaffRequiredMixin,CreateView):
    model = CuentaBancaria
    form_class = FormCuentaBancaria
    extra_context = {'accion': 'Nueva'}
    success_url = reverse_lazy('lista_cuentas')

class EliminarCuentaBancaria(StaffRequiredMixin,DeleteView):
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

class EditarCuentaBancaria(StaffRequiredMixin,UpdateView):
    model = CuentaBancaria
    form_class = FormCuentaBancariaEditar
    extra_context = {'accion': 'Editar'}
    success_url = reverse_lazy('lista_cuentas')

class Bienvenida(TemplateView):
    template_name = 'home.html'

