from django.contrib.auth.models import User
from api.models import Ticket, Message
from rest_framework import status
from rest_framework.test import APITestCase, APIClient


class TicketTestCase(APITestCase):
    """Testing action with tickets."""
    # fixtures = ['my_fixtures.json']

    def setUp(self):
        user_test1 = User.objects.create_user(username='test1', password='qazWSX', email='123@mail.ru')
        user_test1.save()
        user_test2 = User.objects.create_user(username='test2', password='WSXzaq', email='123@mail.ru')
        user_test2.save()
        user_test3 = User.objects.create_user(username='test3', password='zxcASD', email='123@mail.ru', is_staff=True)
        user_test3.save()

        ticket1 = Ticket.objects.create(first_name='123',
                                        id=30,
                                        author=user_test1,
                                        last_name='sdf',
                                        email='zp23buslen@mail.ru',
                                        phone='+375298394807', title='remont',
                                        text='When we fixed my problems?')
        ticket1.save()

    def test_ticket_list(self):
        """Testing jwt auth and ticket list view."""
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
        self.assertEqual(len(resp.data['results']), 1)

        # get ticket list another author
        resp = self.client.post('http://127.0.0.1:8000/auth/jwt/create/', {'username': 'test2', 'password': 'WSXzaq'},
                                format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in resp.data)
        token = resp.data['access']
        client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        resp = client.get('http://127.0.0.1:8000/api/v1/tickets/', data={'format': 'json'})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data['results']), 0)

        # testing access to a ticket when the user is not the author
        resp = client.get('http://127.0.0.1:8000/api/v1/tickets/30/', data={'format': 'json'})
        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(resp.json().get('detail'), "You do not have permission to perform this action.")

    def test_create_ticket(self):
        """Testing ticket creation."""
        resp = self.client.post('http://127.0.0.1:8000/auth/jwt/create/',
                                {'username': 'test1', 'password': 'qazWSX'},
                                format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in resp.data)
        token = resp.data['access']

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        resp = client.post('http://127.0.0.1:8000/api/v1/tickets/', {"first_name": "Test1",
                                                                     "last_name": "Tester",
                                                                     "email": "zpbuslen@mail.ru",
                                                                     "phone": "+375298394804",
                                                                     "title": "remont",
                                                                     "text": "When we fixed my problems?"}, format= 'json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(resp.json().get('title'), "remont")

    def test_change_ticket_status(self):
        """Testing change ticket status when user.is_staff."""
        resp = self.client.post('http://127.0.0.1:8000/auth/jwt/create/',
                                {'username': 'test3', 'password': 'zxcASD'},
                                format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in resp.data)
        token = resp.data['access']

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        resp = client.put('http://127.0.0.1:8000/api/v1/tickets/30/', {"status": "Ticket frozen"}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.json().get('status'), "Ticket frozen")

