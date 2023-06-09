from rest_framework.test import APITestCase
from rest_framework import status
from projects.models import Projects
from django.contrib.auth.models import User


class ProjectListCreateViewTest(APITestCase):
    def setUp(self):
        adam = User.objects.create_user(username='adam', password='123')

    def test_can_retrieve_project_list(self):
        response = self.client.get('/projects/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_create_projects(self):
        self.client.login(username='adam', password='123')
        response = self.client.post('/projects/', {'title': 'a title'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        count = Projects.objects.count()
        self.assertEqual(count, 1)
    
    def test_non_logged_in_user_cant_create_posts(self):
        response = self.client.post('/projects/', {'title': 'a title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class ProjectDetailViewTest(APITestCase):
    def setUp(self):
        adam = User.objects.create_user(username='adam', password='123')
        brian = User.objects.create_user(username='brian', password='123')
        project_1 = Projects.objects.create(title='a title', owner=adam)

    def test_can_retrieve_project_with_valid_id(self):
        response = self.client.get('/projects/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_cant_retrieve_project_with_invalid_id(self):
        response = self.client.get('/projects/2/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_user_can_update_own_projects(self):
        self.client.login(username='adam', password='123')
        response = self.client.put('/projects/1/', {'title': 'a new title'})
        project = Projects.objects.filter(pk=1).first()
        self.assertEqual(project.title, 'a new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_user_cant_update_others_projects(self):
        self.client.login(username='brian', password='123')
        response = self.client.put('/projects/1/', {'title': 'a new title'})
        project = Projects.objects.filter(pk=1).first()
        self.assertEqual(project.title, 'a title')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)