from django.test import TestCase
from django.core.urlresolvers import reverse

from rest_framework.test import APIClient
from rest_framework import status

from maker.models import PasswordResetToken


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


class AuthenticationTest(TestCase):

    url = reverse('authentication')

    def setUp(self):
        self.client = APIClient()
        self.client.post(reverse('registration'), {
            'email': 'test@test.com',
            'password': 'something secret',
            'first_name': 'Testy',
            'last_name': 'McTesterson'
        }, format='json')

    def testSuccess(self):
        response = self.client.post(self.url, {
            'identifier': 'test@test.com',
            'password': 'something secret'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def testMissingIdentifier(self):
        response = self.client.post(self.url, {
            'password': 'something secret'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def testMissingPassword(self):
        response = self.client.post(self.url, {
            'identifier': 'test@test.com'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def testBadCredentials(self):
        response = self.client.post(self.url, {
            'identifier': 'test@test.com',
            'password': 'not the password'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class PasswordResetRequestTest(TestCase):

    url = reverse('password-reset')

    def setUp(self):
        self.client = APIClient()
        self.client.post(reverse('registration'), {
            'email': 'test@test.com',
            'password': 'something secret',
            'first_name': 'Testy',
            'last_name': 'McTesterson'
        }, format='json')

    def testSuccess(self):
        response = self.client.post(self.url, {
            'email': 'test@test.com'
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        token = PasswordResetToken.objects.get(maker__email='test@test.com')
        self.assertEqual(token.maker.email, 'test@test.com')

    def testInvalidEmail(self):
        response = self.client.post(self.url, {
            'email': 'not an email'
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def testEmailDoesNotExist(self):
        response = self.client.post(self.url, {
            'email': 'test1@test.com'
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        try:
            token = PasswordResetToken.objects.get(maker__email='test1@test.com')
        except PasswordResetToken.DoesNotExist:
            pass


