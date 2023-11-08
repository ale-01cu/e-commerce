from django.db import models
from apps.user.models import UserAccount
from apps.product.models import Product
from simple_history.models import HistoricalRecords
from django.core.validators import MinValueValidator, MaxValueValidator

class Comments(models.Model):
    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
        
    rating = models.PositiveIntegerField(
        verbose_name='Valoracion', 
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    
    comment = models.TextField(
        verbose_name='Comentario'
    )
    
    status = models.BooleanField(
        verbose_name='Estado', 
        default=True
    )
    
    product = models.ForeignKey(
        Product, 
        related_name='comments', 
        on_delete=models.CASCADE, 
        verbose_name='Productos'
    )
    
    user = models.ForeignKey(
        UserAccount, 
        related_name='comments', 
        on_delete=models.CASCADE, 
        verbose_name='Usuario'
    )
    
    create_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Fecha de creado'
    )
    
    history = HistoricalRecords()
        
    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by =value
        
    def __str__(self) -> str:
        return self.comment

    