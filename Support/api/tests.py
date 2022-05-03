from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase, APIClient


class TicketTests(APITestCase):
    """Testing jwt auth and ticket list view"""

    def test_ticket_list(self):

        user_test1 = User.objects.create_user(username='test1', password='qazWSX', email='123@mail.ru')
        user_test1.save()

        resp = self.client.post('http://127.0.0.1:8000/auth/jwt/create/', {'username': 'test1', 'password': 'qazWSX'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in resp.data)
        token = resp.data['access']

        client = APIClient()

        client.credentials(HTTP_AUTHORIZATION='Token ' + 'abc')
        resp = client.get('http://127.0.0.1:8000/api/v1/tickets/', data={'format': 'json'})
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

        client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        resp = client.get('http://127.0.0.1:8000/api/v1/tickets/', data={'format': 'json'})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data['results']), 0)
