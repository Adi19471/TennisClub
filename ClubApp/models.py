import email
from django.db import models

# Create your models here.
class Contact(models.Model):
 name = models.CharField(max_length=150)
 email = models.EmailField(max_length=150)
 mobile_number = models.CharField(max_length=10)
 address = models.TextField()
 
 def __str__(self):
  return self.name
 
 
 

# Create your models here.
class User(models.Model):
 name = models.CharField(max_length=70)
 email = models.EmailField(max_length=100)
 password = models.CharField(max_length=100)
 
 


class Book_ground(models.Model):
 
    name = models.CharField(max_length=20)
    date = models.DateField()
    email = models.EmailField()
    time = models.TimeField()
    mobile = models.CharField(max_length=10)
    address = models.CharField(max_length=10)
    
  