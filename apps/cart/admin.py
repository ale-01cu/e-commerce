from django.contrib import admin
from .models import Cart,CartItem

class CartItemAdmin(admin.TabularInline):
    model = CartItem
    extra = 1
    
class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemAdmin]
    list_display = ('id','user')
    list_display_links = ('id','user')
    search_fields = ('id','user',)
    list_per_page = 25

admin.site.register(Cart, CartAdmin)
