from django.test import TestCase
from wger.core.tests.base_testcase import WorkoutManagerTestCase


class SocialLoginTestCase(WorkoutManagerTestCase):
    '''
    Tests the social login functionality
    '''
    def test_google_login(self):
        url = '/accounts/login/google-oauth2/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_facebook_login(self):
        url = '/accounts/login/facebook/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_twitter_login(self):
        url = '/accounts/login/twitter/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
