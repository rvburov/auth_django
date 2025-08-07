from django.test import TestCase, override_settings
from django.urls import reverse
from unittest.mock import patch
from .models import OAuthUser

class OAuthTests(TestCase):
    @patch('requests.post')
    @patch('requests.get')
    def test_google_oauth_flow(self, mock_get, mock_post):
        # Тестирование полного цикла OAuth
        pass
    
    @override_settings(OAUTH_PROVIDERS={
        'google': {'client_id': 'test', 'client_secret': 'test'}
    })
    def test_google_auth_url(self):
        response = self.client.get(reverse('google-auth'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('accounts.google.com', response.url)
