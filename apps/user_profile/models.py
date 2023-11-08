from django.db import models
from .actions import generate_photo_profile_path
from django.contrib.auth import get_user_model
from .choices import ProvinceChoices, TypePhoneNumberChoices
User = get_user_model()    

class UserProfile(models.Model):
    class Meta:
        verbose_name = 'Perfíl de usuario'
        verbose_name_plural = 'Perfiles de usuarios'
        
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        verbose_name='Usuario', 
        related_name='user_profile'
    )
    
    photo = models.ImageField(
        upload_to=generate_photo_profile_path, 
        blank=True, 
        null=True, 
        default='', 
        verbose_name='Foto de perfíl'
    )
    
    address = models.CharField(
        max_length=255, 
        verbose_name='Dirección', 
        blank=True, 
        null=True, 
        default=''
    )
    
    province = models.CharField(
        max_length=255, 
        verbose_name='Provincia', 
        choices=ProvinceChoices.choices, 
        null=True, 
        blank=True, 
        default=''
    )
    
    municipality = models.CharField(
        max_length=255, 
        verbose_name='Municipio', 
        blank=True, 
        null=True
    )
        
    def __str__(self) -> str:
        return self.user.email
