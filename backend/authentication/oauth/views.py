import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import redirect
from django.conf import settings
from .models import OAuthUser
from .serializers import OAuthCallbackSerializer
from .providers.google import GoogleProvider
from .providers.yandex import YandexProvider

class OAuthBaseView(APIView):
    provider_class = None
    
    def get(self, request):
        provider = self.provider_class()
        auth_url = provider.get_auth_url()
        return redirect(auth_url)

class GoogleOAuthView(OAuthBaseView):
    provider_class = GoogleProvider

class YandexOAuthView(OAuthBaseView):
    provider_class = YandexProvider

class OAuthCallbackView(APIView):
    def get(self, request):
        serializer = OAuthCallbackSerializer(data=request.GET)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        code = serializer.validated_data['code']
        provider = request.GET.get('provider', 'google')
        
        try:
            if provider == 'google':
                user_data = GoogleProvider().get_user_info(code)
            elif provider == 'yandex':
                user_data = YandexProvider().get_user_info(code)
            else:
                return Response({'error': 'Invalid provider'}, status=400)
            
            # Создание/обновление пользователя
            oauth_user, created = OAuthUser.objects.update_or_create(
                provider=provider,
                provider_id=user_data['id'],
                defaults={
                    'email': user_data['email'],
                    'user': self._get_or_create_user(user_data)
                }
            )
            
            return redirect(f"{settings.FRONTEND_URL}/oauth-success/")
            
        except Exception as e:
            return redirect(f"{settings.FRONTEND_URL}/oauth-error/?message={str(e)}")

    def _get_or_create_user(self, user_data):
        pass
