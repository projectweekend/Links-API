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
            'identifier': 'something_cool',
            'password': 'something secret',
            'email': 'test@test.com',
            'first_name': 'Testy',
            'last_name': 'McTesterson'
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
