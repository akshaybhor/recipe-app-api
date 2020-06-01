from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email(self):
        email = 'abc@gmail.com'
        password = '123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser(
            'abc@gmail.com',
            'abc123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
