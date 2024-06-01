from django.conf import settings  # type: ignore
from django.shortcuts import render, redirect  # type: ignore
from django.urls import reverse_lazy  # type: ignore
from django.views.generic import ListView  # type: ignore
from .models import Proyecto
from django.views.generic.edit import CreateView  # type: ignore
from django.views.generic.edit import UpdateView, DeleteView  # type: ignore
from .forms import FormProyecto, FormProyectoEditar, FiltrosProyecto
from django.contrib.auth.mixins import LoginRequiredMixin  # type: ignore
from proyectofinal2023.utils import StaffRequiredMixin
from django.http import HttpResponse  # type: ignore
from django.template.loader import render_to_string  # type: ignore
from weasyprint import HTML, CSS  # type: ignore
import datetime


class ListaProyectos(LoginRequiredMixin, ListView):
    model = Proyecto
    extra_context = {'form': FiltrosProyecto}


class NuevoProyecto(StaffRequiredMixin, CreateView):
    model = Proyecto
    form_class = FormProyecto
    extra_context = {'accion': 'Nuevo'}
    success_url = reverse_lazy('lista_proyectos')

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_staff:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)


class EliminarProyecto(StaffRequiredMixin, DeleteView):
    model = Proyecto
    success_url = reverse_lazy('lista_proyectos')

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_staff:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)


def eliminar_todos(request):
    if request.method == 'POST':
        for num_proyecto in request.POST:
            if num_proyecto == "csrfmiddlewaretoken":
                continue
            elif num_proyecto == "todos":
                Proyecto.objects.all().delete()
                return redirect('lista_proyectos')
            Proyecto.objects.get(num_proyecto=num_proyecto).delete()

    return redirect('lista_proyectos')


class EditarProyecto(StaffRequiredMixin, UpdateView):
    model = Proyecto
    form_class = FormProyectoEditar
    extra_context = {'accion': 'Editar'}
    success_url = reverse_lazy('lista_proyectos')

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_staff:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)


def buscar_proyecto(request):
    proyecto = (
        Proyecto.objects.all().order_by(
            'num_proyecto', 'nombre_proyecto'))

    if request.method == 'POST':

        form = FiltrosProyecto(request.POST)
        # num_proyecto = request.POST.get('num_proyecto',None)
        nombre_proyecto = request.POST.get('nombre_proyecto', None)
        # objetivo = request.POST.get('objetivo',None)
        # presupuesto = request.POST.get('presupuesto',None)
        # duracion = request.POST.get('duracion',None)
        responsables = request.POST.get('responsables', None)
        proveedor = request.POST.get('proveedor', None)
        if nombre_proyecto:
            proyecto = proyecto.filter(nombre_proyecto=nombre_proyecto)
        if responsables:
            proyecto = proyecto.filter(responsables=responsables)
        if proveedor:
            proyecto = proyecto.filter(proveedor=proveedor)

    else:
        form = FiltrosProyecto()

    context = {
        'form': form
    }
    return render(request, 'proyecto/proyecto_list.html', context)


def generar_reporte(request):
    # Obtén la fecha actual
    fecha_actual = datetime.date.today()

    # Obtén los datos del modelo
    datos_modelo = Proyecto.objects.all()

    # Obtén el último número de reporte generado
    ultimo_num_reporte = getattr(settings, 'ULTIMO_NUM_REPORTE', 0)

    # Incrementa el número de reporte para el nuevo reporte
    nuevo_num_reporte = ultimo_num_reporte + 1

    # Actualiza el último número de reporte en la configuración
    settings.ULTIMO_NUM_REPORTE = nuevo_num_reporte

    # Obtén los datos adicionales que necesitas para el reporte
    context = {
        'titulo': 'Reporte Proyectos',
        'fecha': fecha_actual,
        'datos_modelo': datos_modelo,
        'num_reporte': nuevo_num_reporte,
    }

    # Renderiza el template HTML con los datos
    html_string = render_to_string('reporte_proyectos.html', context)

    # Crea un objeto de tipo HTML con el contenido renderizado
    html = HTML(string=html_string)

    # Aplica una configuración de CSS adicional para el formato horizontal
    css = CSS(string='''
        @page {
            size: landscape;
        }
    ''')

    # Genera el archivo PDF a partir del objeto HTML con la configuración CSS
    pdf_file = html.write_pdf(stylesheets=[css])

    # Devuelve el archivo PDF como respuesta
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = \
        'attachment; filename="reporte_proyectos.pdf"'
    response.write(pdf_file)

    return response
