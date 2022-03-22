from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin , BaseUserManager

# Create your models here.

class UserProfileManager(BaseUserManager): #heredo la clase base user manager
    '''Manager para perfiles de usuario'''

    def create_user(self, email, name, passwd=None):
        '''crear nuevo user profile'''
        if not email: 
            raise ValueError('usuario debe tener un email')
        
        email = self.normalize_email(email)
        user = self.model(email = email, name = name)
        user.set_password(passwd)
        user.save(using = self._db)
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.save(using = self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin): #heredo las clases abstract base user y permision mixin
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    
    objects = UserProfileManager()
    
    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['name'] 

    def get_full_name(self): 
        return self.name
    
    def get_short_name(self): 
        return self.name 

    def __str__(self): 
        ''' retornar cadena representando usuario'''
        return self.email