from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.

class Account(AbstractBaseUser):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    username=models.CharField(max_length=50,unique=True)
    email=models.EmailField(max_length=50,unique=True)
    phone_number=models.CharField(max_length=50)
