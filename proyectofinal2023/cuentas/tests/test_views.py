from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User, Group
from proyecto.models import Proyecto
from proveedores.models import Proveedor, Estado, Municipio
from cuentas.models import CuentaBancaria
from costos.models import Costo

class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.staff_user = User.objects.create_user(username='staffuser', password='testpassword', is_staff=True)
        # Crear instancias de Estado
        estado = Estado.objects.create(nombre="Estado de Ejemplo")

        # Crear instancias de Municipio asociadas al Estado creado anteriormente
        municipio = Municipio.objects.create(nombre="Municipio de Ejemplo", estado=estado)

        # Crear instancia de Proveedor
        proveedor = Proveedor.objects.create(
        rfc="ABC123456789",
        razon_social="Proveedor de Prueba",
        direccion="Calle de prueba",
        telefono=1234567890,
        correo="proveedor@example.com",
        estado= estado,
        municipio= municipio,
        )

        self.proyecto = Proyecto.objects.create(
            num_proyecto='12345678',
            nombre_proyecto='Proyecto de Prueba',
            objetivo='Objetivo de prueba',
            presupuesto=1500000,
            duracion=12,
            responsables='Responsable de Prueba',
            proveedor= proveedor
        )

        self.costo = Costo.objects.create(descripcion='Costo de Prueba', costo=100.0, proyecto=self.proyecto)

        self.cuenta = CuentaBancaria.objects.create(
        idcuenta='12345678',
        responsable='Responsable de Prueba',
        limite_presupuestario=1500000,
        proyecto=self.proyecto  
    )
        
        # Asegurarse de que el grupo "Investigadores" exista
        Group.objects.get_or_create(name='Investigadores')

    def test_lista_cuentas_view(self):
        response = self.client.get(reverse('lista_cuentas'))
        self.assertIn(response.status_code, [200, 302])

    def test_nueva_cuenta_view(self):
        data = {
            'idcuenta': '87654321',
            'responsable': 'Nuevo Responsable',
            'limite_presupuestario': 2000000,
            'proyecto': self.proyecto
        }
        response = self.client.post(reverse('agregar_cuenta'), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(CuentaBancaria.objects.count(), 1)

    def test_eliminar_cuenta_view(self):
        response = self.client.post(reverse('eliminar_cuenta', args=[self.cuenta.idcuenta]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(CuentaBancaria.objects.count(), 1)

    def test_editar_cuenta_view(self):
        data = {
            'idcuenta': '12345678',
            'responsable': 'Responsable de Prueba',
            'limite_presupuestario': 1500000,
            'proyecto': self.proyecto
        }
        response = self.client.post(reverse('editar_cuenta', args=[self.cuenta.idcuenta]), data)
        self.assertEqual(response.status_code, 302)
        self.cuenta.refresh_from_db()
        self.assertEqual(self.cuenta.responsable, 'Responsable de Prueba')
        self.assertEqual(self.cuenta.limite_presupuestario, 1500000)

    def test_eliminar_cuentas_view(self):
        response = self.client.post(reverse('eliminar_cuentas'), {'todas': ''})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(CuentaBancaria.objects.count(), 0)

    def test_pdf_report_view(self):
        response = self.client.get(reverse('reporte_cuentas'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')

