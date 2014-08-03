from django.core.urlresolvers import reverse

from rest_framework import status

from utils.testing_helpers import AuthenticatedAPITestCase


class LinkSelfTest(AuthenticatedAPITestCase):

    def testSuccess(self):
        # Create without folder
        response = self.client.post(reverse('link-self-list'), {
            'url': 'https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c',
            'note': 'Raspberry Pi GPIO setup tutorial'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['url'], 'https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c')
        self.assertEqual(response.data['note'], 'Raspberry Pi GPIO setup tutorial')

        detail_url = reverse('link-self-detail', args=(response.data['id'],))

        # Create with a folder
        response = self.client.post(reverse('folder-self-list'), {
            'name': 'Arduino Stuff',
            'description': 'Random links about Arduino stuff'
        }, format='json')

        folder = response.data['id']

        response = self.client.post(reverse('link-self-list'), {
            'url': 'https://learn.adafruit.com/flora-and-codebender',
            'note': 'Using Codebender with Flora',
            'folder': folder
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['url'], 'https://learn.adafruit.com/flora-and-codebender')
        self.assertEqual(response.data['note'], 'Using Codebender with Flora')
        self.assertEqual(response.data['folder'], folder)

        # List
        response = self.client.get(reverse('link-self-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 2)

        # Detail
        response = self.client.get(detail_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['url'], 'https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c')

        # Update folder
        response = self.client.patch(detail_url, {
            'folder': folder
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['folder'], folder)

        # Update url
        response = self.client.patch(detail_url, {
            'url': 'https://learn.adafruit.com/collins-lab-soldering'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['url'], 'https://learn.adafruit.com/collins-lab-soldering')

        # Update note
        response = self.client.patch(detail_url, {
            'note': 'Cool video about soldering'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Delete
        response = self.client.delete(detail_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def testInvalidURL(self):
        response = self.client.post(reverse('link-self-list'), {
            'url': 'Not a URL',
            'note': 'Raspberry Pi GPIO setup tutorial'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
