from django.contrib.auth.models import User
from api.models import Ticket, Message
from rest_framework import status
from rest_framework.test import APITestCase, APIClient


class MessageTestCase(APITestCase):
    """Testing action with messages."""
    # fixtures = ['my_fixtures.json']

    def setUp(self):

        user_test1 = User.objects.create_user(username='test1', password='qazWSX', email='123@mail.ru')
        user_test1.save()

        ticket1 = Ticket.objects.create(first_name='123',
                                        id=30,
                                        author=user_test1,
                                        last_name='sdf',
                                        email='zp23buslen@mail.ru',
                                        phone='+375298394807', title='remont',
                                        text='When we fixed my problems?')
        ticket1.save()

        message1 = Message.objects.create(text='Hi', author=user_test1, ticket=ticket1)
        message1.save()

    def test_message_list(self):
        """Testing message list for tickets author."""
        resp = self.client.post('http://127.0.0.1:8000/auth/jwt/create/', {"username": "test1", "password": "qazWSX"}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in resp.data)
        token = resp.data['access']

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        resp = client.get('http://127.0.0.1:8000/api/v1/tickets/30/messages/', data={'format': 'json'})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data['results']), 1)
