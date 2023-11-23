from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(models.Model):
    username = models.CharField(unique=True,max_length=50)
    password = models.CharField(max_length=50)
    def __str__(self):
      return self.username