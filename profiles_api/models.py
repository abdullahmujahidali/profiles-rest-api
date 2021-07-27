from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """ Manager for User Profile """    

    def create_user(self,email,name,password=None):
        """ Create a new user profile """    
        if not email:
            raise ValueError('User must have an email address') 

        email = self.normalize_email(email)
        user = self.model(email=email,name=name)
           




class UserProfile(AbstractBaseUser,PermissionsMixin):
    """ Database model for users in the system """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """ Fetch full name """ 
        return self.name
    
    def get_short_name(self):
        """ Fetch short name """ 
        return self.name

    def __str__(self):
        """ Return string representation of the user """
        return self.email 