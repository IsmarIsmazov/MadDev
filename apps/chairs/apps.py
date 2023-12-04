from django.apps import AppConfig


class ChairsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.chairs'

    def ready(self):
        import apps.chairs.signals
