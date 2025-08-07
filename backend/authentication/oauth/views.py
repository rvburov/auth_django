from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .providers.google import get_google_user_info
from .serializers import OAuthCallbackSerializer

class GoogleOAuthView(APIView):
    def get(self, request):
        # Редирект на Google OAuth
        from urllib.parse import urlencode
        params = {
            'client_id': settings.OAUTH_PROVIDERS['google']['client_id'],
            'redirect_uri': settings.OAUTH_REDIRECT_URI,
            'scope': ' '.join(settings.OAUTH_PROVIDERS['google']['scopes']),
            'response_type': 'code',
        }
        url = f"{settings.OAUTH_PROVIDERS['google']['authorize_url']}?{urlencode(params)}"
        return Response({'url': url})

class OAuthCallbackView(APIView):
    def get(self, request):
        serializer = OAuthCallbackSerializer(data=request.query_params)
        if serializer.is_valid():
            code = serializer.validated_data['code']
            # Обмен code на токен и получение данных пользователя
            # ...
            return Response({'detail': 'OAuth successful'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
