from django.db import models
from django.contrib.auth.models import User 
from django.db.models.signals import post_save
# Create your models here.


class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=250, blank=True)
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(
        upload_to='images/', default='../default-pic_ls0v0g.png'
    )

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"${self.name}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
