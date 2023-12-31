from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    
    # el username debe ser UNICO
    
    GENDER_CHOICES = (
        ('M','MASCULINO'),
        ('F','FEMENINO'),
        ('O','OTROS'),
    )
    username = models.CharField(max_length=50, unique=True) 
    email = models.EmailField()
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    genero = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    
    USERNAME_FIELD = 'username'
    
    def get_short_name(self):
        return self.username
    
    def get_full_name(self):
        return self.nombres+' '+self.apellidos
    
    
    
