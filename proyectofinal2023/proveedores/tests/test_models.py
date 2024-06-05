from django.test import TestCase
from proveedores.models import Proveedor, Estado, Municipio
from django.core.exceptions import ValidationError


class TestProveedorModels(TestCase):
    def setUp(self):
        self.estado = Estado.objects.create(nombre='Estado de México')

        self.municipio = Municipio.objects.create(
            nombre='Municipio de México', estado=self.estado)

        self.proveedor = Proveedor(
            rfc='1234567890123',
            razon_social='Proveedora',
            direccion='Dirección',
            telefono='1234567890',
            correo='correo@correo',
            estado=self.estado,
            municipio=self.municipio
        )

    def test_crear_proveedor(self):
        self.assertEqual(self.proveedor.rfc, '1234567890123')
        self.assertEqual(self.proveedor.razon_social, 'Proveedora')
        self.assertEqual(self.proveedor.direccion, 'Dirección')

    def test_crear_estado(self):
        self.assertEqual(self.estado.nombre, 'Estado de México')

    def test_crear_municipio(self):
        self.assertEqual(self.municipio.nombre, 'Municipio de México')
        self.assertEqual(self.municipio.estado, self.estado)

    def test_str_metodos(self):
        self.assertEqual(str(self.proveedor), 'Proveedora')
        self.assertEqual(str(self.estado), 'Estado de México')
        self.assertEqual(str(self.municipio), 'Municipio de México')

    def test_rfc_unico(self):
        proveedor = Proveedor(
            rfc='1234567890123',
            razon_social='Proveedora 2',
            direccion='Dirección 2',
            telefono='1234567891',
            correo='correo@correo2',
            estado=self.estado,
            municipio=self.municipio
        )
        with self.assertRaises(ValidationError):
            proveedor.full_clean()

    def test_longitud_maxima_campos(self):
        proveedor = Proveedor(
            rfc='1' * 14,
            razon_social='Proveedora muy larga' * 20,
            direccion='Dirección muy larga' * 20,
            telefono='1' * 16,
            correo='correo@correo.com',
            estado=self.estado,
            municipio=self.municipio
        )
        with self.assertRaises(ValidationError):
            proveedor.full_clean()

    def test_proveedor_rfc_requerido(self):
        proveedor = Proveedor(
            razon_social='Proveedora',
            direccion='Dirección',
            telefono='1234567890',
            correo='correo@correo.com',
            estado=self.estado,
            municipio=self.municipio
        )
        with self.assertRaises(ValidationError):
            proveedor.full_clean()

    def test_proveedor_razon_social_requerido(self):
        proveedor = Proveedor(
            rfc='1234567890123',
            direccion='Dirección',
            telefono='1234567890',
            correo='correo@correo.com',
            estado=self.estado,
            municipio=self.municipio
        )
        with self.assertRaises(ValidationError):
            proveedor.full_clean()

    def test_proveedor_direccion_requerido(self):
        proveedor = Proveedor(
            rfc='1234567890123',
            razon_social='Proveedora',
            telefono='1234567890',
            correo='correo@correo.com',
            estado=self.estado,
            municipio=self.municipio
        )
        with self.assertRaises(ValidationError):
            proveedor.full_clean()

    def test_proveedor_telefono_requerido(self):
        proveedor = Proveedor(
            rfc='1234567890123',
            razon_social='Proveedora',
            direccion='Dirección',
            correo='correo@correo.com',
            estado=self.estado,
            municipio=self.municipio
        )
        with self.assertRaises(ValidationError):
            proveedor.full_clean()

    def test_proveedor_correo_requerido(self):
        proveedor = Proveedor(
            rfc='1234567890123',
            razon_social='Proveedora',
            direccion='Dirección',
            telefono='1234567890',
            estado=self.estado,
            municipio=self.municipio
        )
        with self.assertRaises(ValidationError):
            proveedor.full_clean()

    def test_proveedor_estado_requerido(self):
        proveedor = Proveedor(
            rfc='1234567890123',
            razon_social='Proveedora',
            direccion='Dirección',
            telefono='1234567890',
            correo='correo@correo.com',
            municipio=self.municipio
        )
        with self.assertRaises(ValidationError):
            proveedor.full_clean()

    def test_proveedor_municipio_requerido(self):
        proveedor = Proveedor(
            rfc='1234567890123',
            razon_social='Proveedora',
            direccion='Dirección',
            telefono='1234567890',
            correo='correo@correo.com',
            estado=self.estado
        )
        with self.assertRaises(ValidationError):
            proveedor.full_clean()

    def test_estado_nombre_requerido(self):
        estado = Estado()
        with self.assertRaises(ValidationError):
            estado.full_clean()

    def test_municipio_nombre_requerido(self):
        municipio = Municipio(estado=self.estado)
        with self.assertRaises(ValidationError):
            municipio.full_clean()

    def test_municipio_estado_requerido(self):
        municipio = Municipio(nombre='Municipio de México')
        with self.assertRaises(ValidationError):
            municipio.full_clean()

    def test_proveedor_rfc_erroneo(self):
        proveedor = Proveedor(
            rfc='123. ',
            razon_social='Proveedora',
            direccion='Dirección',
            telefono='1234567890',
            correo='correo@correo.com',
            estado=self.estado,
            municipio=self.municipio
        )
        with self.assertRaises(ValidationError):
            proveedor.full_clean()

    def test_proveedor_telefono_erroneo(self):
        proveedor = Proveedor(
            rfc='1234567890123',
            razon_social='Proveedora',
            direccion='Dirección',
            telefono='123j',
            correo='correo@correo.com',
            estado=self.estado,
            municipio=self.municipio
        )
        with self.assertRaises(ValidationError):
            proveedor.full_clean()

    def test_proveedor_correo_erroneo(self):
        proveedor = Proveedor(
            rfc='1234567890123',
            razon_social='Proveedora',
            direccion='Dirección',
            telefono='1234567890',
            correo='correoinvalido',
            estado=self.estado,
            municipio=self.municipio
        )
        with self.assertRaises(ValidationError):
            proveedor.full_clean()

    def test_estado_nombre_erroneo(self):
        estado = Estado(nombre='')
        with self.assertRaises(ValidationError):
            estado.full_clean()

    def test_municipio_nombre_erroneo(self):
        municipio = Municipio(nombre='', estado=self.estado)  # Nombre vacío
        with self.assertRaises(ValidationError):
            municipio.full_clean()
