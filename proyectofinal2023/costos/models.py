from django.db import models
from django.core.validators import MinValueValidator, MaxLengthValidator
from proyecto.models import Proyecto

class Costo(models.Model):
    descripcion = models.CharField(max_length=255, validators=[MaxLengthValidator(255)])
    costo = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        validators=[MinValueValidator(0)]
    )
    proyecto = models.ForeignKey(
        Proyecto,
        verbose_name='Proyecto',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.descripcion
