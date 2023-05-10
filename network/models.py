from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    followers = models.ManyToManyField('self', related_name='following', symmetrical=False, blank=True)
    pic = models.CharField(max_length=500, default="https://www.kindpng.com/picc/m/24-248253_user-profile-default-image-png-clipart-png-download.png")
    def __str__(self):
        return f"{self.username}"


## Creating a Post model

class Post(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=2000)
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    

    def __str__(self):
        return f"{self.user}::::{self.title}"
