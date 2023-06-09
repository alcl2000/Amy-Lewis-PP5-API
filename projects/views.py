from django.shortcuts import render
from .models import Projects
from .serializer import ProjectSerializer
from crack_it_api.permissions import IsOwnerOrReadOnly
from rest_framework import generics, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend


class ProjectList(generics.ListCreateAPIView):
    queryset = Projects.objects.all().order_by('created_on')
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_fields = [
        'owner'
    ]
    search_fields = [
        'title',
        'owner'   
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Projects.objects.all().order_by('created_on')