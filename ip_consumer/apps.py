from django.apps import AppConfig


class IpConsumerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "ip_consumer"

    def ready(self):
        import ip_consumer.signals
