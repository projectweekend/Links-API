from django.test import TestCase
from django.core.urlresolvers import reverse

from rest_framework.test import APIClient
from rest_framework import status


class RegistrationTest(TestCase):

    url = reverse('registration')

    def setUp(self):
        self.client = APIClient()

    def testSuccess(self):
        response = self.client.post(self.url, {
            'email': 'test@test.com',
            'password': 'something secret',
            'first_name': 'Testy',
            'last_name': 'McTesterson'
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def testInvalidEmail(self):
        response = self.client.post(self.url, {
            'email': 'not an email',
            'password': 'something secret',
            'first_name': 'Testy',
            'last_name': 'McTesterson'
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def testNoPassword(self):
        response = self.client.post(self.url, {
            'email': 'test@test.com',
            'first_name': 'Testy',
            'last_name': 'McTesterson'
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def testNoFirstName(self):
        response = self.client.post(self.url, {
            'email': 'test@test.com',
            'password': 'something secret',
            'last_name': 'McTesterson'
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def testNoLastName(self):
        response = self.client.post(self.url, {
            'email': 'test@test.com',
            'password': 'something secret',
            'first_name': 'Testy',
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
