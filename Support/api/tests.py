from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from django.urls import reverse


class TicketTests(APITestCase):

    def SetUp(self):
        user_test1 = User.objects.create_user(username='test1', password='ctrc2ctrcQAZ', email='123@mail.ru')
        user_test1.save()
        user_test2 = User.objects.create_user(username='test2', password='ctrc2ctrcQAZ', email='123@mail.ru')
        user_test2.save()

        # self.one_ticket = Ticket.objects.create(
        #     first_name='Paul',
        #     author=user_test1,
        #     last_name='Tic',
        #     email='123123sdf@mail.ru',
        #     phone='213123213123',
        #     address='Moscow',
        #     title='Expensive',
        #     text='It is so expensive'
        # )

        self.data = {
            'first_name': 'Test1',
            'author': 'Nickname',
            'last_name': 'Test1',
            'email': 'test_email@gmail.com',
            'phone': 'test_phone_123',
            'address': 'Kemerovo',
            'title': 'Some title',
            'text': 'Some text'
        }

    def test_ticket_list(self):
        resp = self.client.post('http://127.0.0.1:8000/auth/jwt/create/', {'username': 'test1', 'password': 'ctrc2ctrcQAZ'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in resp.data)
        token = resp.data['token']

        resp = self.client.post('api/v1/auth/jwt/verify/', {'token': token}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token' + token)
        resp = client.get('/api/v1/tickets/', data={'format': 'json'})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data['results']), 1)
