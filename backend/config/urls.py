from django.contrib import admin
from django.urls import path, include
from config.api_keys import APIKeyTestView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Authentication URLs
    path('auth/', include('authentication.jwt.urls')),
    path('oauth/', include('authentication.oauth.urls')),
    
    # Users URLs
    path('users/', include('users.urls')),
    
    # API документация
    path('docs/', include('docs.docs_config')),

    # Защищённый эндпоинт с API-ключом
    path('api/secure/data/', APIKeyTestView.as_view(), name='secure-api'),
]
