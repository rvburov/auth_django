from django.apps import AppConfig

class JWTConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authentication.jwt'
    verbose_name = 'JWT Аутентификация'
