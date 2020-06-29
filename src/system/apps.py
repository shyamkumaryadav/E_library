from django.apps import AppConfig
from django.db.models.signals import post_migrate


class SystemConfig(AppConfig):
	name = 'system'
	verbose_name = 'E_library System'

	def ready(self):
		import system.signals as ss
		post_migrate.connect(
			ss.create_genre,
			sender=self
		)

