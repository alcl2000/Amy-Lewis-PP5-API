from django.db import models
from django.contrib.auth.models import User


class Projects(models.Model):
    """Creates the project model for the proect app"""
    # progress status
    status_choices = [
        ('todo', 'To do'),
        ('in_progress', 'In Progress'),
        ('finished', 'Finished')
    ]
    # colour choices
    project_color_choices = [
        ('red', 'Red'),
        ('orange', 'Orange'),
        ('yellow', 'Yellow'),
        ('green', 'Green'),
        ('blue', 'Blue'),
        ('purple', 'Purple'),
    ]
    # creation fields
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    # user edited fields
    title = models.CharField(max_length=50)
    goal_1 = models.CharField(max_length=250)
    goal_2 = models.CharField(max_length=250)
    goal_3 = models.CharField(max_length=250)
    deadline = models.DateTimeField(null=True)
    status = models.CharField(
        max_length=11,
        default='todo',
        choices=status_choices
    )
    color = models.CharField(
            max_length=6,
            default='red',
            choices=project_color_choices
                            )
    
