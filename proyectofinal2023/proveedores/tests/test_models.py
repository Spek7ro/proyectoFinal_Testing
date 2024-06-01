from django.test import TestCase
from proveedores.models import Proveedor, Estado, Municipio

class TestProveedorModels(TestCase):
    def test_crear_proveedor(self):
        estado = Estado.objects.create(nombre='Estado de México')
        municipio = Municipio.objects.create(nombre='Municipio de México', estado=estado)
        proveedor = Proveedor.objects.create(
            rfc='123456789',
            razon_social='Proveedora',
            direccion='Dirección',
            telefono='1234567890',
            correo='correo@correo',
            estado=estado,
            municipio=municipio
        )
        self.assertEqual(proveedor.rfc, '123456789')
        self.assertEqual(proveedor.razon_social, 'Proveedora')
        self.assertEqual(proveedor.direccion, 'Dirección')