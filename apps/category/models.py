from django.db import models
from .actions import generate_category_photo_path

class Category(models.Model):
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        
    name = models.CharField(
        max_length=255, 
        verbose_name='Nombre', 
        unique=True
    )
    
    photo = models.ImageField(
        verbose_name='Foto de Categoria', 
        upload_to=generate_category_photo_path, 
        null= True
    )
    
    create_date = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='Fecha de creado'
    )
    
    status = models.BooleanField(
        default=True, 
        verbose_name='Estado'
    )
    
    def __str__(self):
        return self.name