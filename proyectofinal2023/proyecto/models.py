from django.db import models
from proveedores.models import Proveedor

class Proyecto(models.Model):
    num_proyecto = models.CharField('NUM Proyecto', max_length=8, primary_key=True)
    nombre_proyecto = models.CharField(max_length=255)
    objetivo = models.CharField(max_length=255)
    presupuesto = models.CharField(max_length=15)
    duracion = models.DecimalField(max_digits=78, decimal_places=2)
    responsables = models.CharField(max_length=200)
    proveedor = models.ForeignKey("proveedores.Proveedor", \
        verbose_name='Proveedor', on_delete=models.CASCADE)
    
    def __str__(slef):
        return slef.nombre_proyecto

