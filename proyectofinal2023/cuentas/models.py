from django.db import models
from proyecto.models import Proyecto

class CuentaBancaria(models.Model):
    responsable = models.CharField(max_length=100)
    limite_presupuestario = models.DecimalField(max_digits=10, decimal_places=2)
    proyecto = models.ForeignKey("proyecto.Proyecto", \
        verbose_name='Proyecto', on_delete=models.DO_NOTHING)

