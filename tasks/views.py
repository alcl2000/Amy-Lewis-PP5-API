from django.shortcuts import render
from tasks.models import Tasks
from django_filters.rest_framework import DjangoFilterBackend
from tasks.serializer import TaskSerializer
from rest_framework import generics, permissions, filters
from crack_it_api.permissions import IsOwnerOrReadOnly
# Create your views here.


class TaskList(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Tasks.objects.order_by('-created_on')
    filterset_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter
    ]
    filterset_fields = [
        'owner',
        'important',
        'project'
    ]
    search_fields = [
        'title',
        'user'
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Tasks.objects.order_by('-created_on')
