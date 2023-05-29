from django.db.models import Count
from django.shortcuts import render
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from crack_it_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializer import ProfileSerializer

# Create your views here.


class ProfileList(generics.ListAPIView):
    """
    Profiles are created automatically when the user instance is created
    List view does not need create view
    """
    queryset = Profile.objects.annotate(
        project_count=Count('owner__projects', distinct=True)
    ).order_by('created_on')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    # filterset_fields = [
    #     'owner__projects__members__profile',
    #     'projects',
    #     'tasks'
    # ]


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Detail/edit/delete view
    """
    queryset = Profile.objects.annotate(
        project_count=Count('owner__projects', distinct=True)
    ).order_by('created_on')
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ProfileSerializer