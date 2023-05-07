from django.db import models

class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)

class CuentaBancaria(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    responsable = models.CharField(max_length=100)
    limite_presupuestario = models.DecimalField(max_digits=10, decimal_places=2)

