from django.contrib.auth import get_user_model
from django.test import TestCase

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
