from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'photo', 'create_date')
    list_display_links = ('name', 'photo')
    search_fields = ('name', 'create_date')
    readonly_fields = ('create_date',)
    list_per_page = 25
    
    
admin.site.register(Category, CategoryAdmin)
