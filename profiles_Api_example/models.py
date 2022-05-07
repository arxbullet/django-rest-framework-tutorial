from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin , BaseUserManager
from django.conf import settings
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
    """la idea de rescribir el usuario en vez de utilizar el que django trae por defecto 
    es poder añadir campos nuevos y funcionalidades que quiza no esten incluidas en el modelo
    por defecto."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    
    objects = UserProfileManager()
    
    #Según la documentación para establecer el campo identificador único del User tenemos que definir lo siguiente:
    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['name'] 

    def get_full_name(self): 
        return self.name
    
    def get_short_name(self): 
        return self.name 

    def __str__(self): 
        ''' retornar cadena representando usuario'''
        return self.email

class ProfileFeedItem(models.Model):
    '''perfil de status update'''

    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete= models.CASCADE
    )

    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        '''retornar el modelo como cadena'''
        return self.status_text

    