from .models import Costo
from django.contrib import messages
from django.db import models
from proyecto.models import Proyecto
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import FiltrosCosto
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from .forms import FormCosto, FormCostoEditar, FiltrosCosto
from django.contrib.auth.mixins import LoginRequiredMixin
from proyectofinal2023.utils import StaffRequiredMixin

class ListaCostos(LoginRequiredMixin,ListView):
    model = Costo
    paginate_by = 5
    extra_context = {'form':FiltrosCosto}

class NuevoCosto(StaffRequiredMixin,CreateView):
    model = Costo
    extra_context = {'accion': 'Nuevo'}
    success_url = reverse_lazy('lista_costos')
    fields = ['descripcion','costo', 'proyecto']
    
    def form_valid(self, form):
        proyecto = form.cleaned_data['proyecto']
        descripcion = form.cleaned_data['descripcion']
        # Calcula el presupuesto restante
        costos_totales = Costo.objects.filter(proyecto=proyecto).aggregate(total=models.Sum('costo'))['total']
        presupuesto_restante = float(proyecto.presupuesto) - float(costos_totales)
        if presupuesto_restante < 0:
            # Presupuesto negativo, agregar mensaje de advertencia
            messages.warning(
                self.request,
                f"El presupuesto del proyecto '{proyecto}' ha superado el límite. ¡Está en negativo! Por lo tanto, el gasto que quiere registrar ( '{descripcion}' ), no se ha guardado."
            )
            return super().form_invalid(form)
        else:
            proyecto.presupuesto =  presupuesto_restante
            proyecto.save()
            return super().form_valid(form)
    
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_staff:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

class EliminarCosto(StaffRequiredMixin,DeleteView):
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

class EditarCosto(StaffRequiredMixin,UpdateView):
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

def buscar_costos(request):
    costos = Costo.objects.all().order_by('id', 'descripcion')
    
    if request.method == 'POST':
        form = FiltrosCosto(request.POST)
        idcosto = request.POST.get('id',None)
        descripcion = request.POST.get('descripcion',None)
        costo = request.POST.get('costo',None)
        proyecto = request.POST.get('proyecto',None)
        if idcosto:
            costos = costos.filter(idcosto__contains=idcosto)
        if descripcion:
            #costos = costos.filter(descripcion__startswith=descripcion)
            #costos = costos.filter(descripcion__contains=descripcion)
            #costos = costos.filter(descripcion__icontains=descripcion)
            costos = costos.get(descripcion__contains=descripcion)
        if costo:
            costos = costos.filter(costo__contains=costo)
        if proyecto:
            costos = costos.filter(proyecto__contains=proyecto)
        
            
        print(costos.query)
            
    else:
        form = FiltrosCosto()
        
    paginator = Paginator(costos, 5)  
    page_number = request.POST.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'object_list': page_obj,
        'page_obj': page_obj,
        'form': form
    } 
    return render(request, 'costos/costo_list.html', context)