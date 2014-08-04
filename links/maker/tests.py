from django.core.urlresolvers import reverse

from rest_framework import status

from maker.models import PasswordResetToken, EmailChangeToken, Maker
from utils.testing_helpers import APITestCase, AuthenticatedAPITestCase


class RegistrationTest(APITestCase):

    url = reverse('registration')

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


class AuthenticationTest(APITestCase):

    url = reverse('authentication')

    def testSuccess(self):
        self.client.post(reverse('registration'), {
            'email': 'test@test.com',
            'password': 'something secret',
            'first_name': 'Testy',
            'last_name': 'McTesterson'
        }, format='json')

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


class PasswordResetRequestTest(APITestCase):

    url = reverse('password-reset')

    def testSuccess(self):
        self.client.post(reverse('registration'), {
            'email': 'test@test.com',
            'password': 'something secret',
            'first_name': 'Testy',
            'last_name': 'McTesterson'
        }, format='json')

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
            PasswordResetToken.objects.get(maker__email='test1@test.com')
        except PasswordResetToken.DoesNotExist:
            pass


class PasswordResetProcessTest(APITestCase):

    url = reverse('password-reset-process')

    def testSuccess(self):
        self.client.post(reverse('registration'), {
            'email': 'test@test.com',
            'password': 'something secret',
            'first_name': 'Testy',
            'last_name': 'McTesterson'
        }, format='json')

        self.client.post(reverse('password-reset'), {
            'email': 'test@test.com'
        }, format='json')

        reset_request = PasswordResetToken.objects.all()[0]

        response = self.client.post(self.url, {
            'token': reset_request.token,
            'new_password': '123456',
            'confirm_password': '123456'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def testMissingToken(self):
        response = self.client.post(self.url, {
            'new_password': '123456',
            'confirm_password': '123456'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def testMissingNewPassword(self):
        response = self.client.post(self.url, {
            'token': 'dummy token',
            'confirm_password': '123456'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def testMissingConfirmPassword(self):
        response = self.client.post(self.url, {
            'token': 'dummy token',
            'new_password': '123456',
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def testPasswordsNotMatching(self):
        response = self.client.post(self.url, {
            'token': 'dummy token',
            'new_password': 'adsfadsf',
            'confirm_password': '123456'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def testInvalidToken(self):
        response = self.client.post(self.url, {
            'token': 'invalid token',
            'new_password': '123456',
            'confirm_password': '123456'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_412_PRECONDITION_FAILED)


class EmailChangeRequestTest(AuthenticatedAPITestCase):

    url = reverse('email-change-request')

    def testSuccess(self):
        response = self.client.post(self.url, {
            'new_email': 'new@email.com'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def testInvalidEmail(self):
        response = self.client.post(self.url, {
            'new_email': 'not an email'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def testEmailInUse(self):
        response = self.client.post(self.url, {
            'new_email': 'test@test.com'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)


class EmailChangeProcessTest(AuthenticatedAPITestCase):

    url = reverse('email-change-process')

    def testSuccess(self):
        self.client.post(reverse('email-change-request'), {
            'new_email': 'new@email.com'
        }, format='json')
        change_request = EmailChangeToken.objects.all()[0]

        response = self.client.post(self.url, {
            'token': change_request.token
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        Maker.objects.get(email='new@email.com')
        Maker.objects.get(identifier='new@email.com')

    def testMissingToken(self):
        response = self.client.post(self.url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def testInvalidToken(self):
        response = self.client.post(self.url, {
            'token': "not a valid token"
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_412_PRECONDITION_FAILED)


class MakerSelfTest(AuthenticatedAPITestCase):

    url = reverse('maker-self')

    def testSuccess(self):
        # Read
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], 'test@test.com')
        self.assertEqual(response.data['first_name'], 'Testy')
        self.assertEqual(response.data['last_name'], 'McTesterson')

        # Update
        response = self.client.patch(self.url, {
            'first_name': 'Dave',
            'last_name': 'Johnson'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], 'Dave')
        self.assertEqual(response.data['last_name'], 'Johnson')

        # Read
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], 'test@test.com')
        self.assertEqual(response.data['first_name'], 'Dave')
        self.assertEqual(response.data['last_name'], 'Johnson')


class MakerProfileTest(AuthenticatedAPITestCase):

    def testSuccess(self):
        # Add folder
        response = self.client.post(reverse('folder-self-list'), {
            'name': 'Test Folder',
            'description': 'A folder for testing'
        }, format='json')

        folder = response.data['id']

        # Add a link
        self.client.post(reverse('link-self-list'), {
            'url': 'http://www.google.com',
            'note': 'This is Google',
            'folder': folder
        }, format='json')

        # List
        response = self.client.get(reverse('maker-profile-list-view'), format='json')
        results = response.data['results']
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(results[0]['email'], 'test@test.com')
        self.assertEqual(len(results[0]['folders']), 1)
        self.assertEqual(len(results[0]['folders'][0]['links']), 1)

        # Detail
        detail_url = reverse('maker-profile-detail-view', args=(results[0]['id'],))
        response = self.client.get(detail_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], 'test@test.com')
        self.assertEqual(len(response.data['folders']), 1)
        self.assertEqual(len(response.data['folders'][0]['links']), 1)
