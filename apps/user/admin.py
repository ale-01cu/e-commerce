from django.contrib import admin
from apps.user.models import UserAccount

class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'email', 
        'phone_number',
        'is_staff', 
        'is_superuser', 
        'is_active', 
        'last_login', 
        'create_date'
    )
    list_display_links = (
        'id', 
        'email',
        'phone_number'
    )
    search_fields = (
        'first_name', 
        'last_name', 
        'email', 
        'phone_number',
        'birthdate',
        'create_date'
    )
    readonly_fields = ('create_date',)
    list_per_page = 25
    
    
admin.site.register(UserAccount, UserAdmin)