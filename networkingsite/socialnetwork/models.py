from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from common.models import BaseModel

# Create your models here.
class User(AbstractBaseUser, BaseModel):
    first_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=150, unique=True)
    password = models.CharField(max_length=50)
    USERNAME_FIELD = 'email'
    
    def __str__(self):
        return str(self.uuid)