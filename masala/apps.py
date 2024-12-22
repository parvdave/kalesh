from django.apps import AppConfig


class MasalaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'masala'

    def ready(self):
        import masala.signals  # This will automatically connect the signal
