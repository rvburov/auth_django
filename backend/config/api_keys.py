from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings
from decouple import config

class APIKeyPermission(BasePermission):
    """Проверка валидности API-ключа"""
    def has_permission(self, request, view):
        # Получаем ключ из заголовка X-API-KEY
        provided_key = request.headers.get('X-API-KEY', '')
        # Сравниваем с ключом из .env
        valid_key = config('API_KEY', default='')
        return provided_key == valid_key

class APIKeyTestView(APIView):
    """Пример защищенного API-эндпоинта"""
    permission_classes = [APIKeyPermission]

    def get(self, request):
        return Response({
            "status": "success",
            "message": "API key authentication successful"
        })
