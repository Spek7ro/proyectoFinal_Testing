from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import CuentaBancaria
from .forms import FormCuentaBancaria, FormCuentaBancariaEditar


class ListaCuentasBancarias(ListView):
    model = CuentaBancaria

class NuevaCuentaBancaria(CreateView):
    model = CuentaBancaria
    form_class = FormCuentaBancaria
    extra_context = {'accion': 'Nueva'}
    success_url = reverse_lazy('lista_cuentas')

class EliminarCuentaBancaria(DeleteView):
    model = CuentaBancaria
    success_url = reverse_lazy('lista_cuentas') 

class EditarCuentaBancaria(UpdateView):
    model = CuentaBancaria
    form_class = FormCuentaBancariaEditar
    extra_context = {'accion': 'Editar'}
    success_url = reverse_lazy('lista_cuentas')

class Bienvenida(TemplateView):
    template_name = 'home.html'

