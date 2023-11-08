from django.db import models
from django.contrib.auth import get_user_model
from apps.product.models import Product
from django.utils import timezone
User = get_user_model()

class History(models.Model):
    class Meta:
        verbose_name = 'Historial'
        verbose_name_plural = 'Historial'
        
    user = models.OneToOneField(                # Usuario al que le pertenece el historial
        User,
        on_delete=models.CASCADE,
        related_name='user_history',
        verbose_name='Usuario'
    )
    
    def update_history(self, product: Product) -> None:
        try:
            
            history_item = self.history_products.filter(
                product=product
            ).first()
            
            if history_item:
                history_item.date_visited = timezone.now()
                history_item.save()
                
            else:
                history_serializer = self.history_products.create(
                    history=self, 
                    product=product
                )
                history_serializer.save()
                
        except Exception as e:
            print("No se pudo actualizar el historial: ", e)
    
    
    def __str__(self):
        return self.user.email
    
    
class HistoryItem(models.Model):
    class Meta:
        verbose_name = 'Historial de producto'
        verbose_name_plural = 'Historial de productos'
        ordering = ('-date_visited',)           # Ordena los productos del historial desde el mas actual hasta el menos
        
    history = models.ForeignKey(                # Historial al que perteneces los productos
        History,
        on_delete=models.CASCADE,
        related_name='history_products',
        verbose_name='Historial',
    )
        
    product = models.ForeignKey(                # El producto del historial
        Product,
        on_delete=models.CASCADE,
        related_name='history_product',
        verbose_name='Productos',
    )
     
    date_visited = models.DateTimeField(        # La fecha y hora en la que fue visto el producto
        auto_now_add=True,
        verbose_name='Fecha de Visitado'
    )
        
    
    def __str__(self) -> str:
        return self.product.name
    