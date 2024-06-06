from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from common.models import BaseModel
from .constants import RequestStatusTypeChoices

# Create your models here.
class User(AbstractBaseUser, BaseModel):
    first_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=150, unique=True)
    password = models.CharField(max_length=50)
    USERNAME_FIELD = 'email'
    
    def __str__(self):
        return str(self.uuid)


    
class FriendRequest(BaseModel):
    from_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='sent_request'
    )
    to_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='received_request'
    )
    status = models.CharField(
        choices=RequestStatusTypeChoices.choices,
        max_length=20,
        null=True
    )

    def __str__(self):
        return str(self.uuid)
    
