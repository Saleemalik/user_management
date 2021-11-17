from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=150, null=False, blank=False, unique=True)
    password = models.CharField( max_length=225)
    email = models.EmailField(null=True,unique=True)
    address = models.TextField()