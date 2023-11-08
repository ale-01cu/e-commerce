from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import Category
import shutil
import os

# Evento para eliminar la imagen de la categoria que fue eliminada
@receiver(pre_delete, sender=Category)
def delete_products_images(sender, instance, **kwargs):
    try:
        images_dir = os.path.join('media', 'images', 'Categorys', instance.name)
        shutil.rmtree(images_dir)
        print("Se elimino la carpeta ", images_dir, " de la categoria ", f'{instance.name}', ' correctamente.')
        
    except FileNotFoundError:
        print("No se encontro la carpeta de la categoria", instance.name)
    
    except Exception as e:
        print(e)