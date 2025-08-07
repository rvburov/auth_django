import requests
from django.conf import settings

class GoogleProvider:
    def get_auth_url(self):
        from urllib.parse import urlencode
        params = {
            'client_id': settings.OAUTH_PROVIDERS['google']['client_id'],
            'redirect_uri': settings.OAUTH_PROVIDERS['google']['redirect_uri'],
            'scope': ' '.join(settings.OAUTH_PROVIDERS['google']['scopes']),
            'response_type': 'code',
            'access_type': 'offline',
            'prompt': 'consent'
        }
        return f"{settings.OAUTH_PROVIDERS['google']['authorize_url']}?{urlencode(params)}"

    def get_user_info(self, code):
        # Обмен code на токен
        token_data = {
            'code': code,
            'client_id': settings.OAUTH_PROVIDERS['google']['client_id'],
            'client_secret': settings.OAUTH_PROVIDERS['google']['client_secret'],
            'redirect_uri': settings.OAUTH_PROVIDERS['google']['redirect_uri'],
            'grant_type': 'authorization_code'
        }
        token_response = requests.post(
            settings.OAUTH_PROVIDERS['google']['token_url'],
            data=token_data
        )
        token_response.raise_for_status()
        access_token = token_response.json()['access_token']
        
        # Получение данных пользователя
        user_response = requests.get(
            settings.OAUTH_PROVIDERS['google']['userinfo_url'],
            params={'access_token': access_token}
        )
        user_response.raise_for_status()
        
        return {
            'id': user_response.json()['sub'],
            'email': user_response.json()['email'],
            'name': user_response.json().get('name', ''),
            'picture': user_response.json().get('picture', '')
        }
