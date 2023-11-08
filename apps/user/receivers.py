from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.user_profile.models import UserProfile
from apps.user.models import UserAccount
from apps.user_history.models import History

# Evento que crea el carrito, el historial y el perfil del usuario que se registra
@receiver(post_save, sender=UserAccount)
def create_user_models(sender, instance, created, **kwargs):
    if created:        
        profile = UserProfile.objects.create(user=instance)
        profile.save()
        
        history = History.objects.create(user=instance)
        history.save()