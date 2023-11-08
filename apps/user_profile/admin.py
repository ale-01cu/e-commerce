from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'user', 
        'user__is_active', 
        'photo', 
        'address', 
        'province', 
        'municipality'
    )
    list_display_links = (
        'id', 
        'user', 
        'address', 
        'province', 
        'municipality'
    )
    search_fields = ('user', 'address', 'province', 'municipality')
    list_per_page = 25
    
    def user__is_active(self, obj):
        return obj.user.is_active
    
    
    user__is_active.boolean = True                  # Cambia el "True" o "False" por un icono en el panel
    user__is_active.short_description = 'Active'    # Escribe "Active" en la descripcion de la columna donde va el campo
    
    
admin.site.register(UserProfile, UserProfileAdmin)
