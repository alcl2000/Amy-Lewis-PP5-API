from django.shortcuts import render
from models.py import Tasks
from django_filters.rest_framework import DjangoFilterBackend
from serializer.py import TaskSerializer
from rest_framework import generics, permissions, filters
# Create your views here.


class TaskList(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Tasks.objects.all().orderby('-created_on')
    # filterset_backends = [ 
    #     filters.SearchFilter,
    #     DjangoFilterBackend
    # ]
    # filterset_fields = [
        
    # ]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)