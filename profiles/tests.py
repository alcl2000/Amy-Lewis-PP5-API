from rest_framework.test import APITestCase
from rest_framework import status
from profiles.models import Profile
from django.contrib.auth.models import User


class ProfileListViewTest(APITestCase):
    def setUp(self):
        adam = User.objects.create_user(username='adam', password='123')

    def test_can_retrieve_profiles_list(self):
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
