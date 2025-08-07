OAUTH_PROVIDERS = {
    'google': {
        'client_id': 'your-google-client-id',
        'client_secret': 'your-google-secret',
        'authorize_url': 'https://accounts.google.com/o/oauth2/auth',
        'token_url': 'https://oauth2.googleapis.com/token',
        'userinfo_url': 'https://www.googleapis.com/oauth2/v3/userinfo',
        'scopes': ['openid', 'email', 'profile']
    },
    'yandex': {
        'client_id': 'your-yandex-client-id',
        'client_secret': 'your-yandex-secret',
        'authorize_url': 'https://oauth.yandex.ru/authorize',
        'token_url': 'https://oauth.yandex.ru/token',
        'userinfo_url': 'https://login.yandex.ru/info',
        'scopes': ['login:email', 'login:info']
    }
}
