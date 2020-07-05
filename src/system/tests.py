from django.test import TestCase
from .models import Genre


class TestGenre(TestCase):
	# def setUp(self):
		# self.genre = Genre.objects.get(name=3)

	def test_time_pass(self):
		self.assertEqual(Genre.objects.get(pk=3).get_name_display(), 'Alternate history')
