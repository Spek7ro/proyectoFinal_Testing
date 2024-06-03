from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from unittest.mock import patch
from ..views import ListaProyectos, NuevoProyecto, EliminarProyecto, EditarProyecto, buscar_proyecto, generar_reporte, eliminar_todos
from django.test import Client

class ProyectoViewsTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client = Client()

    
    def test_lista_proyectos_view(self):
        self.client.force_login(self.user)

        with patch('proyecto.views.Proyecto.objects.all') as mock_all_proyectos:
            mock_all_proyectos.return_value = []
            response = self.client.get(reverse('lista_proyectos'))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'proyecto/proyecto_list.html')

    def test_nuevo_proyecto_view(self):
        request = self.factory.post(reverse('agregar_proyecto'))
        request.user = self.user

        with patch('proyecto.views.FormProyecto') as mock_form_proyecto:
            mock_form_proyecto.return_value.is_valid.return_value = True
            response = NuevoProyecto.as_view()(request)
            self.assertEqual(response.status_code, 302)

    def test_eliminar_proyecto_view(self):
        request = self.factory.post(reverse('eliminar_proyecto', args=[1]))
        request.user = self.user

        with patch('proyecto.views.Proyecto.objects.get') as mock_get_proyecto:
            mock_get_proyecto.return_value = None
            response = EliminarProyecto.as_view()(request, pk=1)
            self.assertEqual(response.status_code, 302)

    def test_editar_proyecto_view(self):
        request = self.factory.post(reverse('editar_proyecto', args=[1]))
        request.user = self.user

        with patch('proyecto.views.Proyecto.objects.get') as mock_get_proyecto:
            mock_get_proyecto.return_value = None
            with patch('proyecto.views.FormProyectoEditar') as mock_form_proyecto_editar:
                mock_form_proyecto_editar.return_value.is_valid.return_value = True
                response = EditarProyecto.as_view()(request, pk=1)
                self.assertEqual(response.status_code, 302)


