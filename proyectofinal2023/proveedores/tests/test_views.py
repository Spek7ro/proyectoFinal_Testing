from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Proveedor, Estado, Municipio

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.lista_proveedores_url = reverse('lista_proveedores')
        self.agregar_proveedor_url = reverse('agregar_proveedor')
        self.editar_proveedor_url = reverse('editar_proveedor', args=[1])  # Asegúrate de reemplazar el argumento con un id de proveedor válido
        self.eliminar_proveedor_url = reverse('eliminar_proveedor', args=[1])  # Asegúrate de reemplazar el argumento con un id de proveedor válido
        self.eliminar_proveedores_url = reverse('eliminar_proveedores')
        self.reporte_proveedores_url = reverse('reporte_proveedores')
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.superuser = User.objects.create_superuser(username='admin', password='12345')

    def test_lista_proveedores_view(self):
        response = self.client.get(self.lista_proveedores_url)
        self.assertEquals(response.status_code, 302)  # Debería redirigir a la página de inicio de sesión

        self.client.login(username='testuser', password='12345')
        response = self.client.get(self.lista_proveedores_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'proveedores/proveedor_list.html')  # Corregir nombre del template

    def test_nuevo_proveedor_view(self):
        self.client.login(username='admin', password='12345')
        response = self.client.get(self.agregar_proveedor_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'proveedores/proveedor_form.html')  # Corregir nombre del template

    def test_editar_proveedor_view(self):
         # Crear un estado válido en la base de datos de prueba
        estado = Estado.objects.create(nombre='Estado de Prueba')

        # Crear un municipio válido en la base de datos de prueba
        municipio = Municipio.objects.create(nombre='Municipio de Prueba', estado=estado)
        # Asegúrate de crear un proveedor de prueba antes de esta prueba
        proveedor = Proveedor.objects.create(rfc='RFC123', razon_social='Proveedor de prueba', direccion='Dirección de prueba', telefono='1234567890', correo='correo@example.com', estado_id=1, municipio_id=1)

        self.client.login(username='admin', password='12345')
        response = self.client.get(self.editar_proveedor_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'proveedores/proveedor_form.html')  # Corregir nombre del template

    def test_eliminar_proveedor_view(self):
        # Asegúrate de crear un proveedor de prueba antes de esta prueba
        proveedor = Proveedor.objects.create(rfc='RFC123', razon_social='Proveedor de prueba', direccion='Dirección de prueba', telefono='1234567890', correo='correo@example.com', estado_id=1, municipio_id=1)

        self.client.login(username='admin', password='12345')
        response = self.client.get(self.eliminar_proveedor_url)
        self.assertEquals(response.status_code, 200)  # Debería devolver un formulario de confirmación
        self.assertTemplateUsed(response, 'proveedores/proveedor_confirm_delete.html')  # Corregir nombre del template

        # Prueba la eliminación real del proveedor
        response = self.client.post(self.eliminar_proveedor_url)
        self.assertEquals(response.status_code, 302)  # Debería redirigir a la lista de proveedores

    def test_eliminar_proveedores_view(self):
        # Asegúrate de crear al menos un proveedor de prueba antes de esta prueba
        proveedor = Proveedor.objects.create(rfc='RFC123', razon_social='Proveedor de prueba', direccion='Dirección de prueba', telefono='1234567890', correo='correo@example.com', estado_id=1, municipio_id=1)

        self.client.login(username='admin', password='12345')
        response = self.client.post(self.eliminar_proveedores_url, {'todos': 'true'})
        self.assertEquals(response.status_code, 302)  # Debería redirigir a la lista de proveedores

    def test_reporte_proveedores_view(self):
        self.client.login(username='admin', password='12345')
        response = self.client.get(self.reporte_proveedores_url)
        self.assertEquals(response.status_code, 200)  # Debería devolver un archivo PDF
        self.assertEquals(response['Content-Type'], 'application/pdf')  # El tipo de contenido debería ser PDF

    # Agrega pruebas similares para otras vistas como Bienvenida, buscar_municipios, etc.
