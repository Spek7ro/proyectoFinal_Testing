from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import Costo

# Función de señal que se ejecutará antes de eliminar un objeto Costo
@receiver(pre_delete, sender=Costo)
def sumar_costo_al_presupuesto(sender, instance, **kwargs):
    proyecto = instance.proyecto
    costo = instance.costo
    proyecto.presupuesto = float(proyecto.presupuesto) + float(costo)
    proyecto.save()