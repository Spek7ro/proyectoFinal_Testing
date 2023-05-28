# from django.db.models.signals import pre_save
# from django.dispatch import receiver
# from .models import Costo
# from django.db import models
# from django.contrib import messages

# def actualizar_presupuesto(sender, instance, **kwargs):
#     proyecto = instance.proyecto
#     costos_totales = Costo.objects.filter(proyecto=proyecto).aggregate(total=models.Sum('costo'))['total']
#     print(str(proyecto.presupuesto), str(costos_totales))
#     presupuesto_actual = float(proyecto.presupuesto) - float(costos_totales)
#     proyecto.presupuesto =  presupuesto_actual
#     if presupuesto_actual < 0 :
#         messages.warning(instance.request, "¡El presupuesto ha sido superado!")
#         pass
        
#     else:
#         proyecto.save() 

# pre_save.connect(actualizar_presupuesto, sender=Costo)