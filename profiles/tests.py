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

    def test_profile_created_automatically_with_user(self):
        self.client.get('/profiles/')
        count = Profile.objects.count()
        self.assertEqual(count, 1)


class ProfileDetailView(APITestCase):
    def setUp(self):
        adam = User.objects.create_user(username='adam', password='123')
        brian = User.objects.create_user(username='brian', password='123')
    
    def test_user_can_retrieve_profile_with_valid_id(self):
        response = self.client.get('/profiles/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_user_cant_retrieve_profile_with_invalid_id(self):
        response = self.client.get('/profiles/3/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_user_can_edit_own_profile(self):
        self.client.login(username='adam', password='123')
        response = self.client.put('/profiles/1/', {'bio': 'hello'})
        profile = Profile.objects.filter(pk=1).first()
        self.assertEqual(profile.bio, 'hello')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

