from django.db.models.signals import (
    post_save, 
    post_delete,
    pre_save
)
from django.dispatch import receiver
from .models import Product
from apps.recommendation_system.recommendations import re_train_model
import threading
import shutil
import os

def re_train_model_recomended_onUpdate(instance):
    old_name = Product.objects.get(pk=instance.pk).name
    old_description = Product.objects.get(pk=instance.pk).description
    old_brand = Product.objects.get(pk=instance.pk).brand.name
    old_keywords = Product.objects.get(pk=instance.pk).keywords
    old_category = Product.objects.get(pk=instance.pk).category.name
    
    if (
        instance.name != old_name or 
        instance.description != old_description or 
        instance.brand.name != old_brand or 
        instance.keywords != old_keywords or 
        instance.category.name != old_category
    ):
        # Reentrena el modelo de recomendacion en un hilo aparte
        # Si se actualiza el nombre del producto, se reentrena el modelo
        # Si se actualiza la descripcion del producto, se reentrena el modelo
        # Si se actualiza la marca del producto, se reentrena el modelo
        # Si se actualiza las keywords del producto, se reentrena el modelo
        # Si se actualiza la categoria del producto, se reentrena el modelo
        re_train_model()
        
    else:
        pass


# Evento que elimina la carpeta de las imagenes del producto cuando se elimina un producto
def delete_products_images(instance):
    images_dir = os.path.join('media', 'images', 'Products', instance.name)
    shutil.rmtree(images_dir)
    print("Se elimino la carpeta ", images_dir, " del producto ", instance.name, ' correctamente.')
    

        
# Evento que reentrena el modelo de recomendacion cuando se actualiza un producto
@receiver(pre_save, sender=Product)
def re_train_model_recomended_onUpdate_signal(sender, instance, **kwargs):
    try:
        if Product.objects.filter(pk=instance.pk).exists():
            thread = threading.Thread(      # Reentrena el modelo de recomendacion en un hilo aparte
                target=re_train_model_recomended_onUpdate, 
                args=(instance,)
            )
            thread.start()
    except Exception as e:
        print("Error al reentrenar el modelo cuando se actualiza un nuevo producto.", e)

# Evento que reentrena el modelo de recomendacion cuando se crea un nuevo producto
@receiver(post_save, sender=Product)
def re_train_model_recomended_onCreate_signal(sender, instance, created, **kwargs):
    if created:
        try:
            thread = threading.Thread(      # Reentrena el modelo de recomendacion en un hilo aparte
                target=re_train_model, 
                args=()
            )
            thread.start()
        except Exception as e:
            print("Error al reentrenar el modelo cuando se crea un nuevo producto.", e)
    else:
        pass


# Evento que reentrena el modelo de recomendacion cuando se elimina un producto
@receiver(post_delete, sender=Product)
def re_train_model_recomended_ondelete_signal(sender, instance, **kwargs):   
    try:
        thread = threading.Thread(      # Reentrena el modelo de recomendacion en un hilo aparte
            target=re_train_model, 
            args=(instance,)
        )
        thread.start()

        delete_products_images(instance)

    except FileNotFoundError:
        print("No se encontro la carpeta del producto", instance.name)

    except Exception as e:
        print("Error al reentrenar el modelo cuando se elimina un producto.", e)
    