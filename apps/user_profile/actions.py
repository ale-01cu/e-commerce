import os

# Genera la ruta donde se va a guardar la imagen de perfil
def generate_photo_profile_path(instance, filename):
    folder_name = f'images/UserProfile/{instance.user.email}/'
    path = os.path.join(folder_name, filename)
    return path