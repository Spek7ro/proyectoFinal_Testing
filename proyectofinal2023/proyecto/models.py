from django.db import models

class Proyecto(models.Model):
    num_proyecto = models.CharField('NUM Proyecto', max_length=8)
    nombre_proyecto = models.CharField(max_length=255)
    objetivo = models.CharField(max_length=255)
    presupuesto = models.CharField(max_length=15)
    duracion = models.DecimalField(max_digits=78, decimal_places=2)
    responsables = models.CharField(max_length=200)

