from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User, Group
from ..models import Costo
from proveedores.models import Proveedor, Estado, Municipio
from proyecto.models import Proyecto


class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.staff_user = User.objects.create_user(
            username='staffuser', password='testpassword', is_staff=True)
        # Crear instancias de Estado
        estado = Estado.objects.create(nombre="Estado de Ejemplo")

        municipio = Municipio.objects.create(
            nombre="Municipio de Ejemplo", estado=estado)

        # Crear instancia de Proveedor
        proveedor = Proveedor.objects.create(
            rfc="ABC123456789",
            razon_social="Proveedor de Prueba",
            direccion="Calle de prueba",
            telefono=1234567890,
            correo="proveedor@example.com",
            estado=estado,
            municipio=municipio,
        )

        self.proyecto = Proyecto.objects.create(
            num_proyecto='12345678',
            nombre_proyecto='Proyecto de Prueba',
            objetivo='Objetivo de prueba',
            presupuesto=1000000,
            duracion=12,
            responsables='Responsable de Prueba',
            proveedor=proveedor
        )
        self.costo = Costo.objects.create(
            descripcion='Costo de Prueba', costo=100.0, proyecto=self.proyecto)

        # Asegurarse de que el grupo "Investigadores" exista
        Group.objects.get_or_create(name='Investigadores')

    def test_lista_costos_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('lista_costos'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'costos/costo_list.html')

    def test_nueva_costo_view(self):
        self.client.login(username='staffuser', password='testpassword')
        data = {
            'descripcion': 'Nuevo Costo de Prueba',
            'costo': 200.0,
            'proyecto': self.proyecto.pk
        }
        response = self.client.post(reverse('agregar_costo'), data)
        self.assertIn(response.status_code, [200, 302])  # Modificación aquí
        self.assertEqual(Costo.objects.count(), 2)

    def test_eliminar_costo_view(self):
        self.client.login(username='staffuser', password='testpassword')
        response = self.client.post(
            reverse('eliminar_costo', args=[self.costo.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Costo.objects.count(), 0)

    def test_editar_costo_view(self):
        self.client.login(username='staffuser', password='testpassword')
        data = {
            'descripcion': 'Costo de Prueba Actualizado',
            'costo': 200.0,
            'proyecto': self.proyecto.pk
        }
        response = self.client.post(
            reverse('editar_costo', args=[self.costo.id]), data)
        self.assertEqual(response.status_code, 302)
        self.costo.refresh_from_db()
        self.assertEqual(self.costo.descripcion, 'Costo de Prueba Actualizado')
        self.assertEqual(self.costo.costo, 200.0)
