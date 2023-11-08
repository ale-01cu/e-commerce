from django.db import models
from apps.product.models import Product
from django.conf import settings
User = settings.AUTH_USER_MODEL

class Cart(models.Model):
    class Meta:
        verbose_name = 'Carrito'
        verbose_name_plural = 'Carritos'
        
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
        verbose_name='Usuario'
    )
    
    total_items = models.IntegerField(
        default=0,
        verbose_name='Total de Productos'
    )
    
    def __str__(self):
        return self.user.email

    
    
class CartItem (models.Model):
    class Meta:
        verbose_name = 'Producto del carrito'
        verbose_name_plural = 'Productos del carrito'
        
    cart = models.ForeignKey(
        Cart, 
        on_delete=models.CASCADE,
        verbose_name='Carrito'
    )
    
    product = models.ForeignKey(
        Product, 
        related_name='Products', 
        on_delete=models.CASCADE,
        verbose_name='Producto'
    )
    
    count = models.IntegerField(
        verbose_name='Cantidad'
    )
    
    def __str__(self):
        return self.product.name