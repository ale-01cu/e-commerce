from django.contrib import admin
from .models import Comments

class CommentsAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'product', 
        'user', 
        'status',
        'rating', 
        'create_date'
    )
    list_display_links = (
        'rating',  
        'product', 
        'user'
    )
    search_fields = (
        'rating', 
        'comment', 
        'product', 
        'user', 
        'create_date'
    )
    readonly_fields = ('create_date',)
    list_per_page = 25
    
admin.site.register(Comments, CommentsAdmin)
