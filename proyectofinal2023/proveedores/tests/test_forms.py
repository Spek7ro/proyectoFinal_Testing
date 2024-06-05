from django.test import TestCase
from proyecto.forms import FormProyecto, FormProyectoEditar, FiltrosProyecto
from proyecto.models import Proyecto
from proveedores.models import Proveedor, Estado, Municipio


class TestFormProyecto(TestCase):

    def setUp(self):
        self.estado = Estado.objects.create(nombre='Estado de México')

        self.municipio = Municipio.objects.create(
            nombre='Municipio de México', estado=self.estado)

        self.proveedor = Proveedor.objects.create(
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
            presupuesto='100000',
            duracion='12',
            responsables='Responsable de Prueba',
            proveedor=self.proveedor
        )
        self.proyecto_data = {
            'num_proyecto': 'PROY111',
            'nombre_proyecto': 'Proyecto de Prueba',
            'objetivo': 'Objetivo de Prueba',
            'presupuesto': 100000,
            'duracion': 12,
            'responsables': 'Responsable de Prueba',
            'proveedor': self.proveedor.id
        }

    def test_form_proyecto_valid(self):
        form = FormProyecto(data=self.proyecto_data)
        if not form.is_valid():
            print(form.errors)
        self.assertTrue(form.is_valid())

    def test_form_proyecto_invalid(self):
        data = self.proyecto_data.copy()
        data['num_proyecto'] = ''  # Invalid data
        form = FormProyecto(data=data)
        self.assertFalse(form.is_valid())

    def test_form_proyecto_editar_valid(self):

        data = {
            'num_proyecto': 'PROY001',
            'nombre_proyecto': 'Proyecto de Prueba',
            'objetivo': 'Objetivo de Prueba Editado',
            'presupuesto': 100000,
            'duracion': 12,
            'responsables': 'Responsable de Prueba',
            'proveedor': self.proveedor
        }
        form = FormProyectoEditar(instance=self.proyecto, data=data)
        self.assertTrue(form.is_valid())

    def test_form_proyecto_editar_invalid(self):
        data = self.proyecto_data.copy()
        data['nombre_proyecto'] = ''  # Invalid data
        form = FormProyectoEditar(instance=self.proyecto, data=data)
        self.assertFalse(form.is_valid())

    def test_filtros_proyecto_form(self):
        form = FiltrosProyecto(data={})
        self.assertTrue(form.is_valid())

    def test_filtros_proyecto_form_with_data(self):
        data = {
            'num_proyecto': 'PROY111',
            'nombre_proyecto': 'Proyecto de Prueba',
            'objetivo': 'Objetivo de Prueba',
            'presupuesto': 100000,
            'duracion': 12,
            'responsables': 'Responsable de Prueba',
            'proveedor': self.proveedor.id
        }
        form = FiltrosProyecto(data=data)
        if not form.is_valid():
            print(form.errors)
        self.assertTrue(form.is_valid())

    def test_filtros_proyecto_form_partial_data(self):
        data = {
            'num_proyecto': 'PROY111',
        }
        form = FiltrosProyecto(data=data)
        self.assertTrue(form.is_valid())
