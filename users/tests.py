from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve
from .forms import CustomUserCreationForm # new
from .views import SignupPageView # new

# Create your tests here.


class CustomUserTests(TestCase):

    def test_create_user(self):
        user = get_user_model()
        user = user.objects.create_user(
            username='vantol',
            email='test@example.com',
            password='tespassword1234'
        )
        self.assertEqual(user.username, 'vantol')
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        user = get_user_model()
        super_user = user.objects.create_superuser(
            username='superuser',
            email='superadmin@email.com',
            password='testpass123'
        )

        self.assertEqual(super_user.username, 'superuser')
        self.assertEqual(super_user.email, 'superadmin@email.com')
        self.assertTrue(super_user.is_active)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_superuser)


class SignupPageTests(TestCase):

    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)

    def test_signup_form(self):  # new
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_signup_view(self):  # new
        view = resolve('/accounts/signup/')

        self.assertEqual(
            view.func.__name__,
            SignupPageView.as_view().__name__
        )