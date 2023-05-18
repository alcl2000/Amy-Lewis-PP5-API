from rest_framework.test import APITestCase
from rest_framework import status
from tasks.models import Tasks
from django.contrib.auth.models import User


class TaskListViewTest(APITestCase):
    def setUp(self):
        User.objects.create_user(username='adam', password='123')
    
    def test_user_can_create_tasks(self):
        adam = User.objects.get(username='adam')
        Tasks.objects.create(title='task 1', important=False)
        response = self.client.get('/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
