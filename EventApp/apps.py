from django.apps import AppConfig


class EventappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'EventApp'
    def ready(self):
        # This ensures template tags are loaded when the app starts
        import EventApp.templatetags.event_filters