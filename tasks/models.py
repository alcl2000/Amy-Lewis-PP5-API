from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from projects.models import Projects


# Create your models here.
class Tasks(models.Model): 
    # set user to a blank array method - stops user from returning null
    def set_no_owner(self):
        return get_user_model().objects.get_or_create(username='')[0]
    progress_options = [
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'), 
        ('complete', 'Complete')
    ]
    owner = models.ForeignKey(User, 
                              on_delete=models.SET(set_no_owner), 
                              blank=True,
                              )
    title = models.CharField(max_length=250)
    project = models.ForeignKey(Projects, 
                                on_delete=models.CASCADE,
                                related_name='tasks',
                                null=True
                                )
    important = models.BooleanField()
    created_on = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True)
    progress = models.CharField(max_length=11, 
                                default='not_started', 
                                choices=progress_options
                                )
    # assets = models.FileField()

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'${self.id}. ${self.title}'
        