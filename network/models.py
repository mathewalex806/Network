from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


## Creating a Post model

class Post(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=2000)
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user}::::{self.title}"
