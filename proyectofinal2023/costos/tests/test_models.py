from django.test import TestCase
from proyecto.models import Proyecto
from proveedores.models import Proveedor, Estado, Municipio
from costos.models import Costo
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

class TestCostoModel(TestCase):
    def setUp(self):
        self.estado = Estado.objects.create(nombre='Estado de México')
        
        self.municipio = Municipio.objects.create(nombre='Municipio de México', estado=self.estado)
            
        proveedor = Proveedor.objects.create(
            rfc='1234567890123',
            razon_social='Proveedora',
            direccion='Dirección',
            telefono='1234567890',
            correo='correo@correo',
            estado=self.estado,
            municipio=self.municipio
        )
        self.proyecto = Proyecto.objects.create(
            num_proyecto='PROY001',
            nombre_proyecto='Proyecto de Prueba',
            objetivo='Objetivo de Prueba',
            presupuesto=100000,
            duracion=12,
            responsables='Responsable de Prueba',
            proveedor=proveedor
        )
        
    def test_crear_costo(self):
        costo = Costo.objects.create(
            descripcion='Costo de Prueba',
            costo=5000.00,
            proyecto=self.proyecto
        )
        self.assertEqual(costo.descripcion, 'Costo de Prueba')
        self.assertEqual(costo.costo, 5000.00)
        self.assertEqual(costo.proyecto, self.proyecto)

    def test_costo_sin_descripcion(self):
        with self.assertRaises(IntegrityError):
            Costo.objects.create(
                descripcion=None,
                costo=5000.00,
                proyecto=self.proyecto
            )

    def test_costo_sin_proyecto(self):
        with self.assertRaises(IntegrityError):
            Costo.objects.create(
                descripcion='Costo de Prueba',
                costo=5000.00,
                proyecto=None
            )

    def test_costo_negativo(self):
        with self.assertRaises(ValidationError):
            costo = Costo(
                descripcion='Costo de Prueba',
                costo=-5000.00,
                proyecto=self.proyecto
            )
            costo.full_clean()

    def test_costo_con_descripcion_demasiado_larga(self):
        descripcion_larga = 'a' * 256
        with self.assertRaises(ValidationError):
            costo = Costo(
                descripcion=descripcion_larga,
                costo=5000.00,
                proyecto=self.proyecto
            )
            costo.full_clean()

    def test_relacion_inversa_proyecto(self):
        costo = Costo.objects.create(
            descripcion='Costo de Prueba',
            costo=7000.00,
            proyecto=self.proyecto
        )
        self.assertIn(costo, self.proyecto.costo_set.all())