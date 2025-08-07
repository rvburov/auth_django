import requests
from django.conf import settings

class YandexProvider:
    def get_auth_url(self):
        from urllib.parse import urlencode
        params = {
            'client_id': settings.OAUTH_PROVIDERS['yandex']['client_id'],
            'redirect_uri': settings.OAUTH_PROVIDERS['yandex']['redirect_uri'],
            'response_type': 'code',
            'scope': ' '.join(settings.OAUTH_PROVIDERS['yandex']['scopes'])
        }
        return f"{settings.OAUTH_PROVIDERS['yandex']['authorize_url']}?{urlencode(params)}"

    def get_user_info(self, code):
        # Обмен code на токен
        token_data = {
            'code': code,
            'client_id': settings.OAUTH_PROVIDERS['yandex']['client_id'],
            'client_secret': settings.OAUTH_PROVIDERS['yandex']['client_secret'],
            'grant_type': 'authorization_code'
        }
        token_response = requests.post(
            settings.OAUTH_PROVIDERS['yandex']['token_url'],
            data=token_data
        )
        token_response.raise_for_status()
        access_token = token_response.json()['access_token']
        
        # Получение данных пользователя
        user_response = requests.get(
            settings.OAUTH_PROVIDERS['yandex']['userinfo_url'],
            headers={'Authorization': f'OAuth {access_token}'}
        )
        user_response.raise_for_status()
        
        return {
            'id': user_response.json()['id'],
            'email': user_response.json()['default_email'],
            'name': user_response.json().get('real_name', ''),
            'login': user_response.json().get('login', '')
        }
