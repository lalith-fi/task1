from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image

# Create your models here.
class User(AbstractUser):
    userchoices=[('Patient','Patient'),('Doctor','Doctor')]
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    username=models.CharField(max_length=255,unique=True)
    profile_pic=models.ImageField(null=True)
    Address=models.TextField(max_length=1050,blank=True)
    user_type=models.CharField(max_length=255,choices=userchoices,default='Patient')
    USERNAME_FIELD='username'
    REQUIRED_FIELDS=[]

    