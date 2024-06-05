from django.test import TestCase
from cuentas.forms import FormCuentaBancaria
from cuentas.forms import FormCuentaBancariaEditar, FiltrosCuenta
from cuentas.models import CuentaBancaria
from proyecto.models import Proyecto
from proveedores.models import Proveedor, Estado, Municipio


class TestFormCuentaBancaria(TestCase):

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
            num_proyecto='PROY001',
            nombre_proyecto='Proyecto de Prueba',
            objetivo='Objetivo de Prueba',
            presupuesto=100000,
            duracion=12,
            responsables='Responsable de Prueba',
            proveedor=self.proveedor
        )

        self.cuenta_bancaria_data = {
            'idcuenta': 'C001',
            'responsable': 'Responsable de Cuenta',
            'limite_presupuestario': 50000.00,
            'proyecto': self.proyecto
        }

    def test_form_cuenta_bancaria_valid(self):
        form = FormCuentaBancaria(data=self.cuenta_bancaria_data)
        if not form.is_valid():
            print(form.errors)
        self.assertTrue(form.is_valid())

    def test_form_cuenta_bancaria_invalid(self):
        data = self.cuenta_bancaria_data.copy()
        data['idcuenta'] = ''  # Invalid data
        form = FormCuentaBancaria(data=data)
        self.assertFalse(form.is_valid())

    def test_form_cuenta_bancaria_editar_valid(self):
        cuenta_bancaria = CuentaBancaria.objects.create(
            idcuenta='C002',
            responsable='Responsable de Cuenta',
            limite_presupuestario=50000.00,
            proyecto=self.proyecto
        )

        data = {
            'idcuenta': 'C002',
            'responsable': 'Responsable de Cuenta Editado',
            'limite_presupuestario': 75000.00,
            'proyecto': self.proyecto
        }
        form = FormCuentaBancariaEditar(instance=cuenta_bancaria, data=data)
        self.assertTrue(form.is_valid())

    def test_form_cuenta_bancaria_editar_invalid(self):
        cuenta_bancaria = CuentaBancaria.objects.create(
            idcuenta='C003',
            responsable='Responsable de Cuenta',
            limite_presupuestario=50000.00,
            proyecto=self.proyecto
        )

        data = {
            'idcuenta': 'C003',
            'responsable': '',  # Invalid data
            'limite_presupuestario': 75000.00,
            'proyecto': self.proyecto
        }
        form = FormCuentaBancariaEditar(instance=cuenta_bancaria, data=data)
        self.assertFalse(form.is_valid())

    def test_filtros_cuenta_form(self):
        form = FiltrosCuenta(data={})
        self.assertTrue(form.is_valid())

    def test_filtros_cuenta_form_with_data(self):
        data = self.cuenta_bancaria_data.copy()
        form = FiltrosCuenta(data=data)
        if not form.is_valid():
            print(form.errors)
        self.assertTrue(form.is_valid())

    def test_filtros_cuenta_form_partial_data(self):
        data = {
            'idcuenta': 'C004',
        }
        form = FiltrosCuenta(data=data)
        self.assertTrue(form.is_valid())
