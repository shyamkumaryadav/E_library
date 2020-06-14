from django.test import TestCase
from .models import Genre


class TestGenre(TestCase):
	def setUp(self):
		Genre.objects.create(name=3)

	def test_time_pass(self):
		genre = Genre.objects.get(name=3)
		self.assertEqual(genre, 'Alternate history')
