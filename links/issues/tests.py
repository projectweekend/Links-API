from django.core.urlresolvers import reverse

from rest_framework import status

from utils.testing_helpers import APITestCase


class ReportedIssuesTest(APITestCase):

    link_id = ''
    user_id = ''

    def setUp(self):
        super(ReportedIssuesTest, self).setUp()

        # Create a user
        response = self.client.post(reverse('registration'), {
            'email': '123@abc.com',
            'password': '123456',
            'first_name': 'Other',
            'last_name': 'User'
        }, format='json')
        token = response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)

        response = self.client.get(reverse('maker-self'), format='json')
        self.user_id = response.data['id']

        # Create a link for the user
        response = self.client.post(reverse('link-self-list'), {
            'url': 'http://www.google.com',
            'note': 'This is a note'
        }, format='json')

        self.link_id = response.data['id']

        # Create my the user we want to make requests with and login in
        response = self.client.post(reverse('registration'), {
            'email': 'test@test.com',
            'password': 'something secret',
            'first_name': 'Testy',
            'last_name': 'McTesterson'
        }, format='json')
        token = response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)

    def testReportLinkSuccess(self):
        response = self.client.post(reverse('report-link-view'), {
            'link': self.link_id
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def testReportUserSuccess(self):
        response = self.client.post(reverse('report-user-view'), {
            'user': self.user_id
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
