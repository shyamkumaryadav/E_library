from django.apps import AppConfig
from django.db.models.signals import post_migrate
from account.signals import create_user


class AccountConfig(AppConfig):
    name = 'account'
    verbose_name = 'Account'

    def ready(self):
        post_migrate.connect(
            create_user,
            sender=self
        )
