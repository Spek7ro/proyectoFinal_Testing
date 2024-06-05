from django.conf import settings  # type: ignore
from django.shortcuts import render, redirect  # type: ignore
from django.urls import reverse_lazy  # type: ignore
from django.views.generic import ListView, TemplateView  # type: ignore
from django.views.generic.edit import CreateView, DeleteView  # type: ignore
from django.views.generic.edit import UpdateView  # type: ignore
from sympy import Q  # type: ignore
from .models import Proveedor, Municipio
from .forms import FormProveedor, FormProveedorEditar, FiltrosProveedor
from django.http import JsonResponse  # type: ignore
from django.contrib.auth.mixins import LoginRequiredMixin  # type: ignore
from proyectofinal2023.utils import StaffRequiredMixin
from django.http import HttpResponse  # type: ignore
from django.template.loader import render_to_string  # type: ignore
from weasyprint import HTML, CSS  # type: ignore
import datetime
from django.contrib.auth.decorators import login_required  # type: ignore


class ListaProveedores(LoginRequiredMixin, ListView):
    model = Proveedor
    extra_context = {'form': FiltrosProveedor}


class NuevoProveedor(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = Proveedor
    form_class = FormProveedor
    extra_context = {'accion': 'Nuevo'}
    success_url = reverse_lazy('lista_proveedores')

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_staff:
            # Redirige
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)


class EliminarProveedor(StaffRequiredMixin, DeleteView):
    model = Proveedor
    success_url = reverse_lazy('lista_proveedores')

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_staff:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)


def eliminar_proveedores(request):
    if request.method == 'POST':
        for id in request.POST:
            if id == "csrfmiddlewaretoken":
                continue
            elif id == "todos":
                Proveedor.objects.all().delete()
                return redirect('lista_proveedores')
            Proveedor.objects.get(id=id).delete()

    return redirect('lista_proveedores')


class EditarProveedor(StaffRequiredMixin, UpdateView):
    model = Proveedor
    form_class = FormProveedorEditar
    extra_context = {'accion': 'Editar'}
    success_url = reverse_lazy('lista_proveedores')

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_staff:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)


class Bienvenida(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('error_404')
        return super().dispatch(request, *args, **kwargs)


def buscar_municipios(request):
    id_estado = request.POST.get('id_estado', None)
    if id_estado:
        municipios = Municipio.objects.filter(estado_id=id_estado)
        data = [{'id': mun.id, 'nombre': mun.nombre} for mun in municipios]
        return JsonResponse(data, safe=False)
    return JsonResponse({'error': 'Parametro Invalido'}, safe=False)


def obtener_filtros(request):
    filtros = {
        'rfc': request.POST.get('rfc', None),
        'razon_social': request.POST.get('razon_social', None),
        'direccion': request.POST.get('direccion', None),
        'telefono': request.POST.get('telefono', None),
        'correo': request.POST.get('correo', None),
        'estado': request.POST.get('estado', None),
        'municipio': request.POST.get('municipio', None),
    }
    return filtros


def filtrar_proveedor(proveedor, filtros):
    """Aplica filtros al queryset de proveedores."""
    for filtro, valor in filtros.items():
        if valor:
            proveedor = aplicar_filtro(proveedor, filtro, valor)
    return proveedor


def aplicar_filtro(proveedor, filtro, valor):
    """Aplica un filtro específico al queryset de proveedores."""
    if filtro == 'rfc':
        return proveedor.filter(
            Q(rfc__contains=valor) | Q(rfc__icontains=valor)
        )
    return proveedor.filter(**{filtro: valor})


def buscar_proveedor(request):
    proveedor = Proveedor.objects.all().order_by('rfc', 'estado')

    if request.method == 'POST':
        form = FiltrosProveedor(request.POST)
        filtros = obtener_filtros(request)
        proveedor = filtrar_proveedor(proveedor, filtros)
    else:
        form = FiltrosProveedor()

    context = {'form': form, 'proveedores': proveedor}
    return render(request, 'proveedores/proveedor_list.html', context)


@login_required
def generar_reporte(request):
    # Obtén la fecha actual
    fecha_actual = datetime.date.today()

    # Obtén los datos del modelo
    datos_modelo = Proveedor.objects.all()

    # Obtén el último número de reporte generado
    ultimo_num_reporte = getattr(settings, 'ULTIMO_NUM_REPORTE', 0)

    # Incrementa el número de reporte para el nuevo reporte
    nuevo_num_reporte = ultimo_num_reporte + 1

    # Actualiza el último número de reporte en la configuración
    settings.ULTIMO_NUM_REPORTE = nuevo_num_reporte

    # Obtén los datos adicionales que necesitas para el reporte
    context = {
        'titulo': 'Reporte Proveedores',
        'fecha': fecha_actual,
        'datos_modelo': datos_modelo,
        'num_reporte': nuevo_num_reporte,
    }

    # Renderiza el template HTML con los datos
    html_string = render_to_string('reporte_proveedores.html', context)

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
    response['Content-Disposition'] =\
        'attachment; filename="reporte_proveedores.pdf"'
    response.write(pdf_file)

    return response
