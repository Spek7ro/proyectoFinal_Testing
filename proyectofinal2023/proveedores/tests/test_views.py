from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.lista_proveedores_url = reverse('lista_proveedores')
        self.agregar_proveedor_url = reverse('agregar_proveedor')
        # Asegúrate de reemplazar el argumento con un id de proveedor válido
        self.editar_proveedor_url = reverse('editar_proveedor', args=[1])
        # Asegúrate de reemplazar el argumento con un id de proveedor válido
        self.eliminar_proveedor_url = reverse('eliminar_proveedor', args=[1])
        self.eliminar_proveedores_url = reverse('eliminar_proveedores')
        self.reporte_proveedores_url = reverse('reporte_proveedores')
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        self.superuser = User.objects.create_superuser(
            username='admin', password='12345')

    def test_lista_proveedores_view(self):
        response = self.client.get(self.lista_proveedores_url)
        # Debería redirigir a la página de inicio de sesión
        self.assertEquals(response.status_code, 302)

        self.client.login(username='testuser', password='12345')
        response = self.client.get(self.lista_proveedores_url)
        self.assertEquals(response.status_code, 200)
        # Corregir nombre del template
        self.assertTemplateUsed(response, 'proveedores/proveedor_list.html')

    def test_nuevo_proveedor_view(self):
        self.client.login(username='admin', password='12345')
        response = self.client.get(self.agregar_proveedor_url)
        self.assertEquals(response.status_code, 200)
        # Corregir nombre del template
        self.assertTemplateUsed(response, 'proveedores/proveedor_form.html')

    def test_editar_proveedor_view(self):

        self.client.login(username='admin', password='12345')
        response = self.client.get(self.editar_proveedor_url)
        self.assertEquals(response.status_code, 200)
        # Corregir nombre del template
        self.assertTemplateUsed(response, 'proveedores/proveedor_form.html')

    def test_eliminar_proveedor_view(self):

        self.client.login(username='admin', password='12345')
        response = self.client.get(self.eliminar_proveedor_url)
        # Debería devolver un formulario de confirmación
        self.assertEquals(response.status_code, 200)
        # Corregir nombre del template
        self.assertTemplateUsed(
            response, 'proveedores/proveedor_confirm_delete.html')

        # Prueba la eliminación real del proveedor
        response = self.client.post(self.eliminar_proveedor_url)
        # Debería redirigir a la lista de proveedores
        self.assertEquals(response.status_code, 302)

    def test_eliminar_proveedores_view(self):
        self.client.login(username='admin', password='12345')
        response = self.client.post(
            self.eliminar_proveedores_url, {'todos': 'true'})
        # Debería redirigir a la lista de proveedores
        self.assertEquals(response.status_code, 302)

    def test_reporte_proveedores_view(self):
        self.client.login(username='admin', password='12345')
        response = self.client.get(self.reporte_proveedores_url)
        # Debería devolver un archivo PDF
        self.assertEquals(response.status_code, 200)
        # El tipo de contenido debería ser PDF
        self.assertEquals(response['Content-Type'], 'application/pdf')
