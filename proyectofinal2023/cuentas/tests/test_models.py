from django.test import TestCase
from proyecto.models import Proyecto
from proveedores.models import Proveedor, Estado, Municipio
from cuentas.models import CuentaBancaria
from django.core.exceptions import ValidationError


class TestCuentaBancariaModel(TestCase):
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
            presupuesto=100000,
            duracion=12,
            responsables='Responsable de Prueba',
            proveedor=self.proveedor
        )

    def test_crear_cuentabancaria(self):
        cuenta_bancaria = CuentaBancaria.objects.create(
            idcuenta='C001',
            responsable='Responsable de Cuenta',
            limite_presupuestario=50000.00,
            proyecto=self.proyecto
        )
        self.assertEqual(cuenta_bancaria.idcuenta, 'C001')
        self.assertEqual(cuenta_bancaria.responsable, 'Responsable de Cuenta')
        self.assertEqual(cuenta_bancaria.limite_presupuestario, 50000.00)
        self.assertEqual(cuenta_bancaria.proyecto, self.proyecto)

    def test_idcuenta_unica(self):
        CuentaBancaria.objects.create(
            idcuenta='C002',
            responsable='Responsable de Cuenta 2',
            limite_presupuestario=30000.00,
            proyecto=self.proyecto
        )
        with self.assertRaises(Exception):
            CuentaBancaria.objects.create(
                idcuenta='C002',
                responsable='Otro Responsable',
                limite_presupuestario=40000.00,
                proyecto=self.proyecto
            )

    def test_relacion_proyecto(self):
        cuenta_bancaria = CuentaBancaria.objects.create(
            idcuenta='103',
            responsable='Responsable de Cuenta 3',
            limite_presupuestario=70000.00,
            proyecto=self.proyecto
        )
        self.assertEqual(cuenta_bancaria.proyecto, self.proyecto)

    def test_limite_presupuestario_positivo(self):
        cuenta_bancaria = CuentaBancaria(
            idcuenta='C004',
            responsable='Responsable de Cuenta 4',
            limite_presupuestario=-1000.00,  # Límite presupuestario negativo
            proyecto=self.proyecto
        )
        with self.assertRaises(ValidationError):
            cuenta_bancaria.full_clean()
