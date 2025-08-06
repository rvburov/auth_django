from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Authentication URLs
    path('auth/', include('authentication.jwt.urls')),
    path('oauth/', include('authentication.oauth.urls')),
    
    # Users URLs
    path('users/', include('users.urls')),
    
    # API Docs
    path('docs/', include('docs.urls')),
]
