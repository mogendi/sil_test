from django.apps import AppConfig


class OrderConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "order"

    def ready(self) -> None:
        import order.signals  # noqa : F401
