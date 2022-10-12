import email
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=250)
    content = models.TextField()
    
    def __str__(self):
        return self.title

class contacttable(models.Model):
    name=models.CharField(max_length=200)        
    email=models.EmailField(max_length=200)        
    suggestion=models.TextField()        
    
    def __str__(self):
        return self.name