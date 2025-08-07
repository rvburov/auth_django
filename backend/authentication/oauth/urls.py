from django.urls import path
from .views import GoogleOAuthView, OAuthCallbackView

urlpatterns = [
    path('google/', GoogleOAuthView.as_view(), name='google-auth'),
    path('yandex/', GoogleOAuthView.as_view(), name='yandex-auth'),
    path('callback/', OAuthCallbackView.as_view(), name='oauth-callback'),
]
