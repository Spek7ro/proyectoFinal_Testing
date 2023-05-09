from django.db import models

class Proveedor(models.Model):
    rfc = models.CharField('R.F.C', max_length=13)
    razon_social = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()
    estado = models.ForeignKey("proveedores.Estado", verbose_name= "Estado", on_delete= models.DO_NOTHING)
    municipio = models.ForeignKey("proveedores.Municipio", verbose_name= "Municipio", on_delete= models.DO_NOTHING)

    def __str__(self):
        return self.razon_social   

class Estado(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return  self.nombre

class Municipio(models.Model):
    nombre = models.CharField(max_length=100)
    estado = models.ForeignKey("proveedores.Estado", verbose_name = "Estado", on_delete= models.DO_NOTHING)

    def __str__(self):
        return  self.nombre
