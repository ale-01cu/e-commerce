from django.db.models.signals import pre_delete, post_save
from django.dispatch import receiver
from .models import UserProfile
import shutil
import os
from PIL import Image

# Evento que elimina la foto de perfil del perfil que fue eliminado
@receiver(pre_delete, sender=UserProfile)
def delete_products_images(sender, instance, **kwargs):
    try:
        images_dir = os.path.join('media', 'images', 'UserProfile', instance.user.email)
        shutil.rmtree(images_dir)
        print("Se elimino la carpeta ", images_dir, " del usuario ", f'{instance.user.email}', ' correctamente.')
        
    except FileNotFoundError:
        print("No se encontro la carpeta del usuario ", {instance.user.email})
    
    except Exception as e:
        print("Error: ", e)
        
        
# Evento que redimensiona la foto de perfil cuando es guardada
@receiver(post_save, sender=UserProfile)
def resize_image(sender, instance, **kwargs):
    if instance.photo:
        with Image.open(instance.photo.path) as img:
            # Redimensiona la imagen a un tamaño máximo de 800x800 píxeles
            img.thumbnail((400, 400))
            img.save(instance.photo.path)