import email
from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    about = models.TextField(max_length=2000)
    degree = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    uni = models.CharField(max_length=100)
    exp = models.CharField(max_length=1000)
    skills = models.CharField(max_length=1000)