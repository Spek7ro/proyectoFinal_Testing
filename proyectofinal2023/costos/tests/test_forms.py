from django.test import TestCase
from costos.forms import FormCosto, FormCostoEditar, FiltrosCosto
from costos.models import Costo
from proyecto.models import Proyecto
from proveedores.models import Proveedor, Estado, Municipio


class TestFormCosto(TestCase):

    def setUp(self):
        self.estado = Estado.objects.create(nombre='Estado de México')
        self.municipio = Municipio.objects.create(
            nombre='Municipio de México', estado=self.estado)

        self.proveedor = Proveedor.objects.create(
            rfc='1234567890123',
            razon_social='Proveedora',
            direccion='Dirección',
            telefono='1234567890',
            correo='correo@correo.com',
            estado=self.estado,
            municipio=self.municipio
        )

        self.proyecto = Proyecto.objects.create(
            num_proyecto='PROY121',
            nombre_proyecto='Proyecto de Prueba',
            objetivo='Objetivo de Prueba',
            presupuesto=100000,
            duracion=12,
            responsables='Responsable de Prueba',
            proveedor=self.proveedor
        )

        self.costo_data = {
            'descripcion': 'Descripción de Prueba',
            'costo': 5000.00,
            'proyecto': self.proyecto,
        }

    def test_form_costo_valid(self):
        form = FormCosto(data=self.costo_data)
        if not form.is_valid():
            print(form.errors)
        self.assertTrue(form.is_valid())

    def test_form_costo_invalid(self):
        data = self.costo_data.copy()
        data['descripcion'] = ''  # Invalid data
        form = FormCosto(data=data)
        self.assertFalse(form.is_valid())

    def test_form_costo_editar_valid(self):
        costo = Costo.objects.create(
            descripcion='Descripción Original',
            costo=5000.00,
            proyecto=self.proyecto
        )

        data = {
            'descripcion': 'Descripción Editada',
            'costo': 7000.00,
            'proyecto': self.proyecto
        }
        form = FormCostoEditar(instance=costo, data=data)
        self.assertTrue(form.is_valid())

    def test_form_costo_editar_invalid(self):
        costo = Costo.objects.create(
            descripcion='Descripción Original',
            costo=5000.00,
            proyecto=self.proyecto
        )

        data = {
            'descripcion': '',  # Invalid data
            'costo': 7000.00,
            'proyecto': self.proyecto
        }
        form = FormCostoEditar(instance=costo, data=data)
        self.assertFalse(form.is_valid())

    def test_filtros_costo_form(self):
        form = FiltrosCosto(data={})
        self.assertTrue(form.is_valid())

    def test_filtros_costo_form_with_data(self):
        data = self.costo_data.copy()
        form = FiltrosCosto(data=data)
        if not form.is_valid():
            print(form.errors)
        self.assertTrue(form.is_valid())

    def test_filtros_costo_form_partial_data(self):
        data = {
            'descripcion': 'Descripción Parcial',
        }
        form = FiltrosCosto(data=data)
        self.assertTrue(form.is_valid())
