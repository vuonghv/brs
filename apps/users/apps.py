from django.apps import AppConfig


class UsersAppConfig(AppConfig):
    name = 'apps.users'
    verbose_name = "User's Profile"

    def ready(self):
        from apps.users import signals
