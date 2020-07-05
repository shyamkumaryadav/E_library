from django.apps import AppConfig
from django.db.models.signals import post_migrate


class AccountConfig(AppConfig):
    name = 'account'
    verbose_name = 'Account'

    def ready(self):
        import account.signals as ss
        post_migrate.connect(
            ss.create_admin,
            sender=self
        )
