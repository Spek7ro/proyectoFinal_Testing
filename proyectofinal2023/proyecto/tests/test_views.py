from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from unittest.mock import patch
from ..models import Proyecto
from proveedores.models import Proveedor, Estado, Municipio
from django.test import Client


class ProyectoViewsTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        self.client = Client()
        # Crear instancias de Estado
        estado = Estado.objects.create(nombre="Estado de Ejemplo")

        municipio = Municipio.objects.create(
            nombre="Municipio de Ejemplo", estado=estado)

        # Crear instancia de Proveedor
        self.proveedor = Proveedor.objects.create(
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
            proveedor=self.proveedor
        )
        self.client.login(username='testuser', password='12345')

    def test_lista_proyectos_view(self):
        self.client.force_login(self.user)

        with patch('proyecto.views.Proyecto.objects.all')as mock_all_proyectos:
            mock_all_proyectos.return_value = []
            response = self.client.get(reverse('lista_proyectos'))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'proyecto/proyecto_list.html')

    def test_nuevo_proyecto_view(self):
        self.client.force_login(self.user)
        data = {
            'nombre': 'Test Project',
            'descripcion': 'Test Description'
        }
        response = self.client.post(reverse('agregar_proyecto'), data)
        self.assertEqual(response.status_code, 302)

    def test_eliminar_proyecto_view(self):
        self.client.force_login(self.user)

        with patch('proyecto.views.Proyecto.objects.get') as mock_get_proyecto:
            mock_get_proyecto.return_value = None
            response = self.client.post(reverse('eliminar_proyecto', args=[1]))
            self.assertEqual(response.status_code, 302)

    def test_editar_proyecto_view(self):
        self.client.force_login(self.user)
        data = {
            'nombre': 'Updated Project',
            'descripcion': 'Updated Description'
        }
        response = self.client.post(reverse('editar_proyecto', args=[1]), data)
        self.assertEqual(response.status_code, 302)

    def test_lista_proyectos_view_filters(self):
        self.client.force_login(self.user)
        data = {
            'nombre_proyecto': 'Test Project',
            'responsables': 'testuser',
            'proveedor': 'Test Provider'
        }
        response = self.client.get(reverse('lista_proyectos'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'proyecto/proyecto_list.html')
