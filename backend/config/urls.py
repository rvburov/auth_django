from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from config.api_keys import APIKeyTestView  # Импорт API Key View

urlpatterns = [
    # Админка
    path('admin/', admin.site.urls),
    
    # Аутентификация
    path('api/auth/', include('authentication.custom_auth.urls')),  # Кастомная аутентификация
    path('api/auth/jwt/', include('authentication.jwt.urls')),     # JWT эндпоинты
    path('api/auth/oauth/', include('authentication.oauth.urls')), # OAuth эндпоинты
    
    # Пользователи
    path('api/users/', include('users.urls')),
    
    # Защищённый API-эндпоинт с ключом
    path('api/secure-endpoint/', APIKeyTestView.as_view(), name='secure-api'),
    
    # Документация API
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
