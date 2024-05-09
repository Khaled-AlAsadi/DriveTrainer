from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class TestViews(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'asadi',
            'password': '111111'
        }
        self.setup_user()

    def setup_user(self):
        User.objects.create_user(**self.credentials)

    def test_trafic_rules_view_deny_anonymous(self):
        response = self.client.get('/trafic_rules', follow=True)
        self.assertRedirects(response, '/login/')

    def test_trafic_rules_view_load(self):
        # Log in
        response_login = self.client.post(
            '/login/', self.credentials, follow=True)

        self.assertTrue(response_login.context['user'].is_active)

        response_traffic_rules = self.client.get('/trafic_rules', follow=True)

        self.assertEqual(response_traffic_rules.status_code, 200)

    def test_road_signs_page_view_deny_anonymous(self):
        response = self.client.get('/road_signs', follow=True)
        self.assertRedirects(response, '/login/')

    def test_login_functionality(self):
        response = self.client.post('/login/', self.credentials, follow=True)

        self.assertTrue(response.context['user'].is_active)
