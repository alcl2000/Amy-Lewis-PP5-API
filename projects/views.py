from django.shortcuts import render
from .models import Projects
from .serializer import ProjectSerializer
from crack_it_api.permissions import IsOwnerOrReadOnly
from rest_framework import generics


class ProjectList(generics.ListCreateAPIView):
    queryset = Projects.objects.order_by('created_on')
    serializer_class = ProjectSerializer


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Projects.objects.all().order_by('created_on')