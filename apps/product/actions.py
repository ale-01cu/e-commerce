import os

# Genera la ruta donde se guarda ka imagen del producto
def generate_product_photo_path(instance, filename):
    folder_name = f'images/Products/{instance.name}/'
    path = os.path.join(folder_name, filename)
    return path

# Genera la ruta donde se guardan las imagenes del producto
def generate_product_images_path(instance, filename):
    folder_name = f'images/Products/{instance.product}/'
    path = os.path.join(folder_name, filename)
    return path