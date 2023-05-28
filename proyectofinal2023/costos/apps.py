from django.apps import AppConfig


class CostoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'costos'
    def ready(self):
        import costos.signals 

