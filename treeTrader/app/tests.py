from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from .models import Dashboard

User = get_user_model()


class TestDashboard(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        user = User.objects.create(username='test_user')
        user.set_password('123')
        self.user = User.objects.get(username='test_user')

    def test_check_main_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_user_can_create_dashboard(self):
        self.client.force_login(self.user)
        response = self.client.post('/new_dashboard', data={'name': 'foo', 'description': 'bar', 'user_id': '1'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Dashboard.objects.count(), 1)

