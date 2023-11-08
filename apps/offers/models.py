from django.db import models
from apps.product.models import Product
from django.core.exceptions import ValidationError

class Offer(models.Model):
    name = models.CharField(
        max_length=255, 
        verbose_name='Nombre de la oferta'
    )
    
    status = models.BooleanField(
        default=True, 
        verbose_name='Estado'
    )
    
    start_date = models.DateTimeField(
        verbose_name='Fecha del inicio de la oferta'
    )
    
    end_date = models.DateTimeField(
        verbose_name='Fecha del fin de la oferta'
    )
    
    create_date = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='Fecha de creado'
    )
    
    class Meta:
        verbose_name = 'Oferta'
        verbose_name_plural = 'Ofertas'
        
    def __str__(self):
        return self.name
    
    
class OfferProduct(models.Model):
    class Meta:
        verbose_name = 'Oferta del producto'
        verbose_name_plural = 'Ofertas de los productos'
        
    class DiscountTypes(models.TextChoices):
        PORCIENTO = '%'
        DINERO = '$'
        
    offer = models.ForeignKey(
        Offer, 
        related_name='offer_product', 
        verbose_name='Oferta', 
        on_delete=models.CASCADE
    )
    
    product = models.ForeignKey(
        Product, 
        related_name='offer', 
        verbose_name='Producto', 
        on_delete=models.CASCADE
    )
    
    discount_type = models.CharField(
        max_length=12 ,
        verbose_name='Tipo de descuento', 
        choices=DiscountTypes.choices
    )
    
    discount = models.FloatField(
        verbose_name='Descuento'
    )
              
    def __str__(self):
        return self.offer.name
    
    def clean(self):
        super().clean()
        
        # Valida que el descuento sea menor que el precio del producto y el 100% ademas de que sea mayor que 0
        if self.discount_type == OfferProduct.DiscountTypes.PORCIENTO:
            if self.discount <= 0 or self.discount >= 100:
                raise ValidationError('El descuento debe estar entre 0 y 100%')
        elif self.discount_type == OfferProduct.DiscountTypes.DINERO:
            if self.discount <= 0 or self.discount >= self.product.price:
                raise ValidationError(f'El descuento debe ser menor al precio del producto (${self.product.price})')
