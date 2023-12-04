from django.apps import AppConfig


class ChairsConfig(AppConfig):
    verbose_name = 'Стулья'
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.chairs'

    def ready(self):
        import apps.chairs.signals
