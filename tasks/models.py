from django.db import models
from django.contrib.auth.models import User
from projects.models import Projects


# Create your models here.
class Tasks(models.Model):
    progress_options = [
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'), 
        ('complete', 'Complete')
    ]
    user = models.ForeignKey(User, 
                             on_delete=models.SET_NULL, 
                             blank=True,
                             null=True
                             )
    title = models.CharField(max_length=250)
    project = models.ForeignKey(Projects, 
                                on_delete=models.CASCADE,
                                related_name='tasks',
                                blank=True,
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
        