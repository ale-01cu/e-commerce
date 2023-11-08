import os

# Genera la ruta de donde va la imagen de la categoria
def generate_category_photo_path(instace, filename):
    folder_name = f'images/Categorys/{instace.name}/'
    path = os.path.join(folder_name, filename)
    return path
