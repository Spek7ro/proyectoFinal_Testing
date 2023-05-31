from django.conf import settings
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import CuentaBancaria
from django.core.paginator import Paginator
from .forms import FormCuentaBancaria, FormCuentaBancariaEditar, FiltrosCuenta
from django.contrib.auth.mixins import LoginRequiredMixin
from proyectofinal2023.utils import StaffRequiredMixin
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML, CSS
import datetime


class ListaCuentasBancarias(LoginRequiredMixin,ListView):
    model = CuentaBancaria
    extra_context = {'form': FiltrosCuenta}

class NuevaCuentaBancaria(StaffRequiredMixin,CreateView):
    model = CuentaBancaria
    form_class = FormCuentaBancaria
    extra_context = {'accion': 'Nueva'}
    success_url = reverse_lazy('lista_cuentas')
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_staff:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

class EliminarCuentaBancaria(StaffRequiredMixin,DeleteView):
    model = CuentaBancaria
    success_url = reverse_lazy('lista_cuentas')
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_staff:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs) 
    
def eliminar_cuentas(request):
    if request.method == 'POST':
        for idcuenta in request.POST:
            if idcuenta == "csrfmiddlewaretoken":
                continue
            elif idcuenta == "todas":
                CuentaBancaria.objects.all().delete()
                return redirect('lista_cuentas')
            CuentaBancaria.objects.get(idcuenta=idcuenta).delete()
    
    return redirect('lista_cuentas')

class EditarCuentaBancaria(StaffRequiredMixin,UpdateView):
    model = CuentaBancaria
    form_class = FormCuentaBancariaEditar
    extra_context = {'accion': 'Editar'}
    success_url = reverse_lazy('lista_cuentas')
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_staff:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

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
            #cuentas = cuentas.filter(proyecto__startswith=proyecto)
            #cuentas = cuentas.filter(proyecto__contains=proyecto)
            #cuentas = cuentas.filter(proyecto__icontains=proyecto)
            cuentas = cuentas.get(proyecto=proyecto)
        if responsable:
            cuentas = cuentas.filter(responsable=responsable)
        if limite_presupuestario:
            cuentas = cuentas.filter(limite_presupuestario__contains=limite_presupuestario)
        
            
        print(cuentas.query)
            
    else:
        form = FiltrosCuenta()
        
    context = {
        'form': form
    } 
    return render(request, 'cuentas/cuentabancaria_list.html', context)

def generar_reporte(request):
    # Obtén la fecha actual
    fecha_actual = datetime.date.today()

    # Obtén los datos del modelo
    datos_modelo = CuentaBancaria.objects.all()

   # Obtén el último número de reporte generado
    ultimo_num_reporte = getattr(settings, 'ULTIMO_NUM_REPORTE', 0)
    
    # Incrementa el número de reporte para el nuevo reporte
    nuevo_num_reporte = ultimo_num_reporte + 1
    
    # Actualiza el último número de reporte en la configuración
    settings.ULTIMO_NUM_REPORTE = nuevo_num_reporte
    
    # Obtén los datos adicionales que necesitas para el reporte
    context = {
        'titulo': 'Reporte Cuentas Bancarias',
        'fecha': fecha_actual,
        'datos_modelo': datos_modelo,
        'num_reporte': nuevo_num_reporte,
    }

    # Renderiza el template HTML con los datos
    html_string = render_to_string('reporte_cuentas.html', context)
    
    # Crea un objeto de tipo HTML con el contenido renderizado
    html = HTML(string=html_string)
    
    # Genera el archivo PDF a partir del objeto HTML con la configuración CSS
    pdf_file = html.write_pdf()
    
     # Devuelve el archivo PDF como respuesta
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte_cuentas.pdf"'
    response.write(pdf_file)
    
    return response