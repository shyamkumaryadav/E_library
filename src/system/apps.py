from django.apps import AppConfig


class SystemConfig(AppConfig):
    name = 'system'
    verbose_name = 'E_library System'

    def ready(self):
        import system.signals
