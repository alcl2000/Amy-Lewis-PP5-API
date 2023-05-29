from django.urls import path
from projects import views

urlpatterns = [
    path('projects/', views.ProjectList.as_view()),
    # path('profiles/<int:pk>/', views.ProfileDetail.as_view())
]