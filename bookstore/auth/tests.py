from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
# Create your tests here.
class AuthenticatonTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        
        self.username = "test"
        self.email = "user@example.com"
        self.password = "string"

    def test_success_register_user(self):
        response = self.client.post(reverse('auth:register'), {"username": self.username, "email": self.email, "password":self.password})
        self.assertEqual(response.status_code, 201)

    def test_login_success_user(self):
        User.objects.create_user(username=self.username, email=self.email, password=self.password)
        response = self.client.post(reverse('auth:login'), {"username": self.username, "password": self.password})
        self.assertEqual(response.status_code, 200)


