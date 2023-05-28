from django.db import models


# Create your models here.
class Costo(models.Model):
    descripcion = models.TextField(max_length=255)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    proyecto = models.ForeignKey("proyecto.Proyecto", \
        verbose_name='Proyecto', on_delete=models.CASCADE)
    

