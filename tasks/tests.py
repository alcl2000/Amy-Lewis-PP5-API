from rest_framework.test import APITestCase
from rest_framework import status
from tasks.models import Tasks
from projects.models import Projects
from django.contrib.auth.models import User


class TaskListViewTest(APITestCase):
    def setUp(self):
        adam = User.objects.create_user(username='adam', password='123')
        Projects.objects.create(id=1, title='project_1', owner=adam)
    
    def test_user_can_retrieve_task_list(self):
        adam = User.objects.get(username='adam')
        response = self.client.get('/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_logged_in_user_can_create_tasks(self):
        self.client.login(username='adam', password='123')
        response = self.client.post('/tasks/', {'title': 'a title'}, project=1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        count = Tasks.objects.count()
        self.assertEqual(count, 1)
    
    def test_non_logged_in_user_cant_create_posts(self):
        response = self.client.post('/tasks/', {'title': 'a title'}, project=1)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class TaskDetailViewTest(APITestCase):

    def setUp(self):
        adam = User.objects.create_user(username='adam', password='123')
        brian = User.objects.create_user(username='brian', password='123')
        project_1 = Projects.objects.create(id=1,
                                            title='project_1',
                                            owner=adam)
        Tasks.objects.create(project=project_1,
                             title='a title',
                             id=1,
                             owner=adam,
                             important=True)
        Tasks.objects.create(project=project_1,
                             id=2,
                             title='another title',
                             owner=brian,
                             important=True)
        
    def test_can_retrieve_task_with_valid_id(self):
        response = self.client.get('/tasks/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

