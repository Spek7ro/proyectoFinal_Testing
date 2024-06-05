from django.test import TestCase
from django.contrib.auth.models import User
from autenticacion.forms import RegistroForm, ReestablecerContraseñaForm
from django.contrib.auth.models import Group


class TestRegistroForm(TestCase):

    def setUp(self):
        Group.objects.get_or_create(name='Investigadores')
        self.user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        }

    def test_registro_form_valid(self):
        form = RegistroForm(data=self.user_data)
        self.assertTrue(form.is_valid())

    def test_registro_form_invalid_email(self):
        data = self.user_data.copy()
        data['email'] = ''  # Invalid email
        form = RegistroForm(data=data)
        self.assertFalse(form.is_valid())

    def test_registro_form_password_mismatch(self):
        data = self.user_data.copy()
        data['password2'] = 'differentpassword'  # Password mismatch
        form = RegistroForm(data=data)
        self.assertFalse(form.is_valid())

    def test_registro_form_existing_user(self):
        User.objects.create_user(
            username='testuser', email='testuser@example.com',
            password='testpassword123')
        form = RegistroForm(data=self.user_data)

        self.assertFalse(form.is_valid())


class TestReestablecerContraseñaForm(TestCase):

    def setUp(self):
        Group.objects.get_or_create(name='Investigadores')

        self.user = User.objects.create_user(
            username='testuser', email='testuser@example.com',
            password='testpassword123')
        self.form_data = {
            'email': 'testuser@example.com',
            'password1': 'newpassword123',
            'password2': 'newpassword123',
        }

    def test_reestablecer_contraseña_form_valid(self):
        form = ReestablecerContraseñaForm(data=self.form_data)
        self.assertTrue(form.is_valid())

    def test_reestablecer_contraseña_form_invalid_email(self):
        data = self.form_data.copy()
        data['email'] = 'invalid@example.com'  # Email does not exist
        form = ReestablecerContraseñaForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_reestablecer_contraseña_form_password_mismatch(self):
        data = self.form_data.copy()
        data['password2'] = 'differentpassword'  # Password mismatch
        form = ReestablecerContraseñaForm(data=data)
        self.assertFalse(form.is_valid())
