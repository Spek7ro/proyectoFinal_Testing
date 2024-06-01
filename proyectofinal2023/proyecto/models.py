from django.db import models  # type: ignore


class Proyecto(models.Model):
    num_proyecto = models.CharField(
        'NUM Proyecto', max_length=8, primary_key=True)
    nombre_proyecto = models.CharField('Nombre del proyecto', max_length=255)
    objetivo = models.TextField('Objetivo')
    presupuesto = models.CharField('Presupuesto ($)', max_length=15)
    duracion = models.TextField('Duracion (Meses)')
    responsables = models.CharField('Responsable', max_length=200)
    proveedor = models.ForeignKey(
        "proveedores.Proveedor",
        verbose_name='Proveedor',
        on_delete=models.CASCADE)

    def __str__(slef):
        return slef.nombre_proyecto
