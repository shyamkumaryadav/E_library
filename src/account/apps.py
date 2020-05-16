from django.apps import AppConfig


class AccountConfig(AppConfig):
    name = 'account'
    verbose_name = 'Member Account'

    def ready(self):
        import account.signals
