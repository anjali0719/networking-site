from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from common.models import BaseModel
from .constants import RequestStatusTypeChoices

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, BaseModel):
    first_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=150, unique=True)
    password = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    
    objects = UserManager()
    # def __str__(self):
    #     return str(self.uuid)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, socialnetwork):
        return True

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def get_username(self):
        return self.email


    
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
    
