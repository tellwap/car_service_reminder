from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager


# Create your models here.

class CustomAccountManager(BaseUserManager):
    def create_user(self,username,first_name, last_name,email,password,**other_fields) :
        if not email:
            raise ValueError('You must provide email address')
        if not username:
            raise ValueError('You must provide username')    

        email = self.normalize_email(email)
        user = self.model(first_name=first_name,last_name=last_name,username=username, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,username,first_name, last_name,email,password,**other_fields) :
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_active',True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is staff=True')

        if other_fields.get('is_superuser') is not True:
          raise ValueError('Superuser must be assigned to is superuser=True')    
     
        return self.create_user(username,first_name,last_name,email,password,**other_fields)  

class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True,null=True)
    phone_number = models.CharField(max_length=255, unique=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name','last_name','email','username']