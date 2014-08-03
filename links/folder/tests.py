from django.core.urlresolvers import reverse

from rest_framework import status

from utils.testing_helpers import AuthenticatedAPITestCase


class FolderSelfTest(AuthenticatedAPITestCase):

    def testSuccess(self):
        # Create
        response = self.client.post(reverse('folder-self-list'), {
            'name': 'Test Folder'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        detail_url = reverse('folder-self-detail', args=(response.data['id'],))

        # List
        response = self.client.get(reverse('folder-self-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)

        # Detail
        response = self.client.get(detail_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Folder')

        # Update name
        response = self.client.patch(detail_url, {
            'name': 'Something Else'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Something Else')

        # Update is_public
        response = self.client.patch(detail_url, {
            'is_public': False
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['is_public'], False)

        # Update description
        response = self.client.patch(detail_url, {
            'description': 'This is the description'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['description'], 'This is the description')

        # Delete
        response = self.client.delete(detail_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def testMissingName(self):
        response = self.client.post(reverse('folder-self-list'), {
            'description': 'This is the description'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def testDuplicateName(self):
        self.client.post(reverse('folder-self-list'), {
            'name': 'Test Folder',
            'description': 'This is the description'
        }, format='json')

        response = self.client.post(reverse('folder-self-list'), {
            'name': 'Test Folder'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)
