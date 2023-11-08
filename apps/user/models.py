from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from simple_history.models import HistoricalRecords
from phonenumber_field.modelfields import PhoneNumberField

class UserAccountManager(BaseUserManager):
    # Metodo que registra el usuario
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El usario no tiene una direccion email')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        
        user.set_password(password)
        user.save()
               
        return user
    
    # Metodo que registra el usuario administrador
    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        
        user.is_superuser = True
        user.is_staff = True
        user.save()
        
        return user
    
    
class UserAccount(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name = 'Cuenta de Usuario'
        verbose_name_plural = 'Cuentas de Usuarios'
        
    email = models.EmailField(
        max_length=255, 
        unique=True,
        verbose_name='Correo'
    )
    
    first_name = models.CharField(
        max_length=255,
        verbose_name='Nombre'
    )
    
    last_name = models.CharField(
        max_length=255,
        verbose_name='Apellidos'
    )
    
    phone_number = PhoneNumberField(
        verbose_name='Numero de Telefono',
        unique=True
    )
    
    birthdate = models.DateField(
        verbose_name='Fecha de nacimineto',
    )
    
    is_active = models.BooleanField(
        default=True,
        verbose_name='Activo',
    )
    
    is_staff = models.BooleanField(
        default=False,
    )
    
    create_date = models.DateTimeField(
        verbose_name='Fecha de creado',
        auto_now_add=True
    )
    
    history = HistoricalRecords()
    objects = UserAccountManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'first_name', 
        'last_name', 
        'phone_number', 
        'birthdate'
    ]

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name
    
    def get_short_name(self):
        return self.first_name
    
    def __str__(self):
        return self.email