from django.test import TestCase
from proveedores.models import Proveedor, Estado, Municipio

class TestProveedorModels(TestCase):
    def setUp(self):
        self.proveedor = Proveedor(
            rfc='123456789',
            razon_social='Proveedora',
            direccion='Dirección',
            telefono='1234567890',
            correo='correo@correo',
            estado=Estado.objects.create(nombre='Estado de México'),
            municipio=Municipio.objects.create(nombre='Municipio de México', estado=Estado.objects.create(nombre='Estado de México'))
        )
        
        self.estado = Estado.objects.create(nombre='Estado de México')
        
        self.municipio = Municipio.objects.create(nombre='Municipio de México', estado=self.estado)
        
    def test_crear_proveedor(self):
        self.assertEqual(self.proveedor.rfc, '123456789')
        self.assertEqual(self.proveedor.razon_social, 'Proveedora')
        self.assertEqual(self.proveedor.direccion, 'Dirección')
        
    def test_crear_estado(self):
        self.assertEqual(self.estado.nombre, 'Estado de México')
        
    def test_crear_municipio(self):
        self.assertEqual(self.municipio.nombre, 'Municipio de México')
        self.assertEqual(self.municipio.estado, 'Estado de México')
        
    def test_crear_proveedor_datos_invalido(self):
        estado = Estado.objects.create(nombre='Estado de México')
        municipio = Municipio.objects.create(nombre='Municipio de México', estado=estado)
        with self.assertRaises(ValueError):
            Proveedor.objects.create(
                rfc='123456789',
                razon_social='Proveedora',
                direccion='Dirección',
                telefono='1234567890',
                correo='correo@correo',
                estado=estado,
                municipio=municipio
            )