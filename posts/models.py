from django.db import models
from users.models import User
# Create your models here.

def image_file_handler(instance,filename):
    return (f"image/{instance}/{filename}")



class Post(models.Model):
    user = models.ForeignKey(User,on_delete= models.CASCADE)
    name = models.CharField(max_length=50)
    content = models.CharField(max_length=450)
    created_at = models.DateTimeField(auto_now_add=True)
    media = models.FileField(upload_to= image_file_handler,blank= True)
    shared_with = models.ManyToManyField(User,related_name= "shared")

    