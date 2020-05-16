from django.test import TestCase
from .models import User


class UserTest(TestCase):

    def setUp(self):
        pass

    def checkUser(self):
        user = User.objects.get(pk=1)
        self.assertEqual(self.user.email, "amin@123.com")
