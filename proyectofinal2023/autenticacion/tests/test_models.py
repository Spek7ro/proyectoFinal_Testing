from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

User = get_user_model()


class UserModelTests(TestCase):
    def setUp(self):
        Group.objects.get_or_create(name='Investigadores')

    def test_create_user(self):

        username = 'testuser'
        email = 'test@example.com'
        password = 'testpassword123'
        user = User.objects.create_user(
            username=username, email=email, password=password)
        self.assertEqual(user.username, username)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):

        username = 'testsuperuser'
        email = 'super@example.com'
        password = 'testpassword123'
        user = User.objects.create_superuser(
            username=username, email=email, password=password)
        self.assertEqual(user.username, username)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

    def test_str_representation(self):

        username = 'testuser'
        email = 'test@example.com'
        password = 'testpassword123'
        user = User.objects.create_user(
            username=username, email=email, password=password)
        self.assertEqual(str(user), username)
