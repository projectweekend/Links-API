from django.test import TestCase
from django.core.urlresolvers import reverse

from rest_framework.test import APIClient


class APITestCase(TestCase):

    def setUp(self):
        self.client = APIClient()


class AuthenticatedAPITestCase(APITestCase):

    def setUp(self):
        super(AuthenticatedAPITestCase, self).setUp()
        self.client.post(reverse('registration'), {
            'email': 'test@test.com',
            'password': 'something secret',
            'first_name': 'Testy',
            'last_name': 'McTesterson'
        }, format='json')
        response = self.client.post(reverse('authentication'), {
            'identifier': 'test@test.com',
            'password': 'something secret'
        }, format='json')
        token = response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
