from django.db import models
from apps.product.models import Product
from .countries import Countries
from django.contrib.auth import get_user_model  
from phonenumber_field.modelfields import PhoneNumberField
from simple_history.models import HistoricalRecords
from apps.user_profile.choices import ProvinceChoices, TypePhoneNumberChoices
from .actions import generate_transactionid
User = get_user_model()

class Order(models.Model):
    class Meta:
        verbose_name = 'Orden'
        verbose_name_plural = 'Ordenes'
        ordering = ['-date_issued']
    
    class OrderStatus(models.TextChoices):
        not_processed = 'not_processed'            #Status: Default   - No procesada la orden. 
        processed = 'processed'                    #Status: Procesada - Cliente de acuerdo con la compra.
        shipping = 'shipped'                       #Status: Envio     - Orden en camino al client.
        delivered = 'delivered'                    #Status: Entregada - Orden recibida por el cliente.
        cancelled = 'cancelled'                    #Status: Cancelada - Cliente cancela el pedido.
    
    order_status = models.CharField(              
        max_length=50, 
        choices=OrderStatus.choices, 
        default=OrderStatus.not_processed, 
        verbose_name='Estado de la orden'
    )
    
    order_number = models.CharField(               
        max_length=255,
        default=generate_transactionid, 
        verbose_name='Numero de Orden', 
        unique = True
    )
    
    user = models.ForeignKey(                                          
        User, 
        on_delete=models.CASCADE, 
        related_name='order_user',
        verbose_name='Usuario'
    )          
           
    first_name = models.CharField(
        verbose_name='Nombre',
        max_length=255
    )     

    last_name = models.CharField(
        verbose_name='Apellido',
        max_length=255
    )                    
    
    address_line_1 = models.CharField(
        verbose_name='Dirección',
        max_length=255
    )                                                            
                    
    province = models.CharField(                                        
        max_length=255, 
        verbose_name='Provincia', 
        choices=ProvinceChoices.choices
    )                               
    
    shipping_price = models.DecimalField(                               
        max_digits=5, 
        decimal_places=2
    )                                
    
    date_issued = models.DateTimeField(                                 
        auto_now_add=True,
        verbose_name='Fecha de creada'
    ) 

    history = HistoricalRecords(verbose_name='Historial de orden')      

    def __str__(self):
        return self.order_number

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
        
    @property
    def amount(self):
        total_amount = 0
        order_items = self.order_items.all()
        
        for item in order_items:
            total_amount += item.count
            
        return total_amount  
    
    @property
    def total_price(self):
        total_price = 0
        order_intems = self.order_items.all()
        
        for item in order_intems:
            discount_price = item.product.discount_price
            if discount_price > 0:
                total_price += discount_price * item.count
            else:
                total_price += item.product.price * item.count
            
        return total_price
    
    @property
    def ten_porcent(self):
        return (self.total_price * 10) / 100


class OrderItem(models.Model):
    class Meta:
        verbose_name = 'Producto de la Orden'
        verbose_name_plural = 'Productos de las Ordenes'
        
    product = models.ForeignKey(
        Product, 
        on_delete=models.DO_NOTHING, 
        related_name='order_item', 
        verbose_name='Producto'
    )
    
    order = models.ForeignKey(
        Order, 
        on_delete=models.CASCADE, 
        related_name='order_items', 
        verbose_name='Orden'
    )        
    
    count = models.PositiveIntegerField(          
        verbose_name='Cantidad de productos'
    )                            
        
    
# class OrderPhoneNumber(models.Model):
#     class Meta:
#         verbose_name = 'Numero telefonico de la Orden'
#         verbose_name_plural = 'Numeros telefonicos de las Ordenes'
#         unique_together = ('phone_number', 'order')
        
#     phone_number = PhoneNumberField()                       
    
#     number_type = models.CharField(                      
#         max_length=255, 
#         choices=TypePhoneNumberChoices.choices, 
#         verbose_name='Tipo de numero'
#     )
    
#     contact_name = models.CharField(
#         max_length=255,
#         verbose_name='Nombre de contacto'
#     )
    
#     order = models.ForeignKey(                     
#         Order, 
#         on_delete=models.CASCADE, 
#         related_name='phone_number',
#         verbose_name='Perfil de Usuario'
#     )

#     def __str__(self):
#         return str(self.phone_number)