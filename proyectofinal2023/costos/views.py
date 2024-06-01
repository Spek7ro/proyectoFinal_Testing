from django.conf import settings
from .models import Costo
from django.contrib import messages
from django.db import models
from proyecto.models import Proyecto
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import FiltrosCosto
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from .forms import FormCosto, FormCostoEditar, FiltrosCosto
from django.contrib.auth.mixins import LoginRequiredMixin
from proyectofinal2023.utils import StaffRequiredMixin
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
import datetime


class ListaCostos(LoginRequiredMixin, ListView):
    model = Costo
    extra_context = {'form': FiltrosCosto}


class NuevoCosto(StaffRequiredMixin, CreateView):
    model = Costo
    extra_context = {'accion': 'Nuevo'}
    success_url = reverse_lazy('lista_costos')
    fields = ['descripcion', 'costo', 'proyecto']

    def form_valid(self, form):
        proyecto = form.cleaned_data['proyecto']
        descripcion = form.cleaned_data['descripcion']
        # Calcula el presupuesto restante
        costos_totales = Costo.objects.filter(proyecto=proyecto).aggregate(
            total=models.Sum('costo'))['total'] or 0
        presupuesto_restante = float(
            proyecto.presupuesto) - float(costos_totales)
        if presupuesto_restante < 0:
            # Presupuesto negativo, agregar mensaje de advertencia
            messages.warning(
                self.request,
                f"El presupuesto del proyecto '{proyecto}' \
                    ha superado el límite. ¡Está en negativo! \
                    Por lo tanto, el gasto que quiere registrar ('{
                    descripcion}'), no se ha guardado."
            )
            return super().form_invalid(form)
        else:
            proyecto.presupuesto = presupuesto_restante
            proyecto.save()
            return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_staff:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)


class EliminarCosto(StaffRequiredMixin, DeleteView):
    model = Costo
    success_url = reverse_lazy('lista_costos')

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_staff:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)


def eliminar_costos(request):
    if request.method == 'POST':
        for id in request.POST:
            if id == "csrfmiddlewaretoken":
                continue
            elif id == "todos":
                Costo.objects.all().delete()
                return redirect('lista_costos')
            Costo.objects.get(id=id).delete()

    return redirect('lista_costos')


class EditarCosto(StaffRequiredMixin, UpdateView):
    model = Costo
    form_class = FormCostoEditar
    extra_context = {'accion': 'Editar'}
    success_url = reverse_lazy('lista_costos')

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_staff:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)


class Bienvenida(TemplateView):
    template_name = 'home.html'


def generar_reporte(request):
    # Obtén la fecha actual
    fecha_actual = datetime.date.today()

    # Obtén los datos del modelo
    datos_modelo = Costo.objects.all()

    # Obtén el último número de reporte generado
    ultimo_num_reporte = getattr(settings, 'ULTIMO_NUM_REPORTE', 0)

    # Incrementa el número de reporte para el nuevo reporte
    nuevo_num_reporte = ultimo_num_reporte + 1

    # Actualiza el último número de reporte en la configuración
    settings.ULTIMO_NUM_REPORTE = nuevo_num_reporte

    # Obtén los datos adicionales que necesitas para el reporte
    context = {
        'titulo': 'Reporte De Costos',
        'fecha': fecha_actual,
        'datos_modelo': datos_modelo,
        'num_reporte': nuevo_num_reporte,
    }

    # Renderiza el template HTML con los datos
    html_string = render_to_string('reporte_costos.html', context)

    # Crea un objeto de tipo HTML con el contenido renderizado
    html = HTML(string=html_string)

    # Genera el archivo PDF a partir del objeto HTML con la configuración CSS
    pdf_file = html.write_pdf()

    # Devuelve el archivo PDF como respuesta
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = \
        'attachment; filename="reporte_costos.pdf"'
    response.write(pdf_file)

    return response
