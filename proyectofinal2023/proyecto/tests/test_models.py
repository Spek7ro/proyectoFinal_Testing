from django.test import TestCase
from django.core.exceptions import ValidationError
from proyecto.models import Proyecto
from proveedores.models import Proveedor, Estado, Municipio


class TestProyectoModels(TestCase):
    def setUp(self):
        self.proveedor = Proveedor.objects.create(
            rfc='1234567890123',
            razon_social='Proveedor Test',
            direccion='Dirección Test',
            telefono='1234567890',
            correo='test@proveedor.com',
            estado=Estado.objects.create(nombre='Estado Test'),
            municipio=Municipio.objects.create(
                nombre='Municipio Test',
                estado=Estado.objects.create(nombre='Estado Test'))
        )

    def test_crear_proyecto(self):
        proyecto = Proyecto.objects.create(
            num_proyecto='PROY001',
            nombre_proyecto='Proyecto de Prueba',
            objetivo='Objetivo de Prueba',
            presupuesto='100000',
            duracion='12',
            responsables='Responsable de Prueba',
            proveedor=self.proveedor
        )
        self.assertEqual(proyecto.num_proyecto, 'PROY001')
        self.assertEqual(proyecto.nombre_proyecto, 'Proyecto de Prueba')
        self.assertEqual(proyecto.objetivo, 'Objetivo de Prueba')
        self.assertEqual(proyecto.presupuesto, '100000')
        self.assertEqual(proyecto.duracion, '12')
        self.assertEqual(proyecto.responsables, 'Responsable de Prueba')
        self.assertEqual(proyecto.proveedor, self.proveedor)

    def test_campos_requeridos(self):
        proyecto = Proyecto()
        with self.assertRaises(ValidationError):
            proyecto.full_clean()

    def test_presupuesto_no_acepta_letras(self):
        proyecto = Proyecto(
            num_proyecto='PROY002',
            nombre_proyecto='Proyecto de Prueba 2',
            objetivo='Objetivo de Prueba 2',
            presupuesto='abc123',  # Presupuesto con letras
            duracion='12',
            responsables='Responsable de Prueba 2',
            proveedor=self.proveedor
        )
        with self.assertRaises(ValidationError):
            proyecto.full_clean()

    def test_rfc_proveedor_asociado(self):
        proyecto = Proyecto(
            num_proyecto='PROY003',
            nombre_proyecto='Proyecto de Prueba 3',
            objetivo='Objetivo de Prueba 3',
            presupuesto='200000',
            duracion='24',
            responsables='Responsable de Prueba 3',
            proveedor=None  # Proveedor no asociado
        )
        with self.assertRaises(ValidationError):
            proyecto.full_clean()

    def test_duracion_numero_valido(self):
        proyecto = Proyecto(
            num_proyecto='PROY004',
            nombre_proyecto='Proyecto de Prueba 4',
            objetivo='Objetivo de Prueba 4',
            presupuesto='300000',
            duracion='doce',
            responsables='Responsable de Prueba 4',
            proveedor=self.proveedor
        )
        with self.assertRaises(ValidationError):
            proyecto.full_clean()

    def test_limite_superior_presupuesto(self):
        proyecto = Proyecto(
            num_proyecto='PROY005',
            nombre_proyecto='Proyecto de Prueba 5',
            objetivo='Objetivo de Prueba 5',
            presupuesto='1000000000000000',
            duracion='12',
            responsables='Responsable de Prueba 5',
            proveedor=self.proveedor
        )
        with self.assertRaises(ValidationError):
            proyecto.full_clean()

    def test_longitud_maxima_campos(self):
        proyecto = Proyecto(
            num_proyecto='PROY007',
            nombre_proyecto='X' * 256,
            objetivo='X' * 1000,
            presupuesto='700000',
            duracion='12',
            responsables='X' * 201,
            proveedor=self.proveedor
        )
        with self.assertRaises(ValidationError):
            proyecto.full_clean()

    def test_relacion_clave_foranea_proveedor(self):
        # Asumiendo que el proveedor ya ha sido creado en el método setUp
        proyecto = Proyecto(
            num_proyecto='PROY008',
            nombre_proyecto='Proyecto de Prueba 8',
            objetivo='Objetivo de Prueba 8',
            presupuesto='800000',
            duracion='12',
            responsables='Responsable de Prueba 8',
            proveedor=self.proveedor
        )
        proyecto.save()  # Guardamos el proyecto
        self.assertEqual(proyecto.proveedor, self.proveedor)

    def test_str_metodos(self):
        proyecto = Proyecto.objects.create(
            num_proyecto='PROY111',
            nombre_proyecto='Proyecto de Prueba',
            objetivo='Objetivo de Prueba',
            presupuesto='100000',
            duracion='12',
            responsables='Responsable de Prueba',
            proveedor=self.proveedor
        )
        self.assertEqual(str(proyecto), 'Proyecto de Prueba')
