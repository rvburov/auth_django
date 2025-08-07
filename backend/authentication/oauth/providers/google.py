import requests
from django.conf import settings
from ..models import OAuthUser

def get_google_user_info(access_token):
    response = requests.get(
        settings.OAUTH_PROVIDERS['google']['userinfo_url'],
        params={'access_token': access_token}
    )
    if response.status_code == 200:
        data = response.json()
        return OAuthUser(
            provider='google',
            email=data.get('email'),
            name=data.get('name'),
            picture=data.get('picture')
        )
    return None
