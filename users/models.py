from django.db import models
from django.contrib.auth.models import AbstractUser 
# Create your models here.

class User(AbstractUser):
    phone_number = models.CharField(unique = True,max_length=18,blank=True)



class UserProfile(models.Model):
    user = models.OneToOneField(User , on_delete= models.CASCADE, null=True)
    bio = models.CharField(max_length=150,null= True,blank=True)
    dob= models.DateField(null= True,blank=True)
    city = models.CharField(max_length=20,null= True,blank=True)
