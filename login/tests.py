from django.test import TestCase, Client
from django.contrib.auth.models import User

# Create your tests here.


class LoginTests(TestCase):

    def test_login(self):
        client = Client()
        u = User.objects.create_user(username='whatsup', password='nothingmuch')
        u.save()
        login = client.login(username='whatsup', password='nothingmuch')
        self.assertTrue(login)