from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User, Group
from django.contrib.messages import get_messages

class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.group = Group.objects.create(name='Investigadores')
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
            email='testuser@example.com',
            first_name='Test',
            last_name='User'
        )
        self.login_url = reverse('iniciar_sesion')
        
    def test_user_added_to_investigadores_group(self):
        user = User.objects.create_user(username='pruebaGrupo', password='grupo123')

        investigadores_group = Group.objects.get(name='Investigadores')
        self.assertIn(investigadores_group, user.groups.all())

    def test_vregistro_get(self):
        response = self.client.get(reverse('Autenticacion'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registro/registro.html')

    def test_vregistro_post_valid(self):
        form_data = {
            'username': 'newuser',
            'password1': 'newpassword123',
            'password2': 'newpassword123',
            'first_name': 'New',
            'last_name': 'User',
            'email': 'newuser@example.com'
        }
        response = self.client.post(reverse('Autenticacion'), data=form_data)
        self.assertEqual(response.status_code, 302)  # Should redirect
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_vregistro_post_invalid(self):
        form_data = {
            'username': 'newuser',
            'password1': 'newpassword123',
            'password2': 'wrongpassword',
            'first_name': 'New',
            'last_name': 'User',
            'email': 'newuser@example.com'
        }
        response = self.client.post(reverse('Autenticacion'), data=form_data)
        self.assertEqual(response.status_code, 200)  # Should not redirect
        self.assertFalse(User.objects.filter(username='newuser').exists())

    def test_cerrar_sesion(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('cerrar_sesion'))
        self.assertEqual(response.status_code, 302)  # Should redirect
        self.assertFalse('_auth_user_id' in self.client.session)

    def test_error404(self):
        response = self.client.get(reverse('error_404'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, '404.html')
        
    def test_invalid_user_shows_error_message(self):
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'wrongpassword'  # Contraseña incorrecta para un usuario existente
        })

        # Verificar que la respuesta contiene el mensaje de error
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Información incorrecta")

    def test_incorrect_information_shows_error_message(self):
        # Enviar un formulario vacío o con datos inválidos
        response = self.client.post(self.login_url, {
            'username': '',  # Campo vacío
            'password': ''
        })
        
        # Verificar que la respuesta contiene el mensaje de error
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Información incorrecta")
        
    def test_loguear_post_valid(self):
        form_data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        response = self.client.post(reverse('iniciar_sesion'), data=form_data)
        self.assertEqual(response.status_code, 302)  # Should redirect
        self.assertTrue('_auth_user_id' in self.client.session)

    def test_loguear_post_invalid(self):
        form_data = {
            'username': 'testuser',
            'password': 'wrongpassword'
        }
        response = self.client.post(reverse('iniciar_sesion'), data=form_data)
        self.assertEqual(response.status_code, 200)  # Should not redirect
        self.assertFalse('_auth_user_id' in self.client.session)

    def test_reestablecer_contraseña_post_valid(self):
        form_data = {
            'email': 'testuser@example.com',
            'password1': 'newpassword123',
            'password2': 'newpassword123'
        }
        response = self.client.post(
            reverse('reestablecer_contra'), data=form_data)
        self.assertEqual(response.status_code, 302)  # Should redirect
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password('newpassword123'))

    def test_reestablecer_contraseña_post_invalid(self):
        form_data = {
            'email': 'nonexistent@example.com',
            'password1': 'newpassword123',
            'password2': 'newpassword123'
        }
        response = self.client.post(
            reverse('reestablecer_contra'), data=form_data)
        self.assertEqual(response.status_code, 302)  # Should redirect
        self.user.refresh_from_db()
        self.assertFalse(self.user.check_password('newpassword123'))
