from django.contrib import admin
from .models import Offer, OfferProduct

class OfferProductAdmin(admin.TabularInline):
    model = OfferProduct
    extra = 1

class OfferAdmin(admin.ModelAdmin):
    inlines = [OfferProductAdmin]
    list_display = (
        'name', 
        'status', 
        'start_date', 
        'end_date', 
        'create_date'
    )
    list_display_links = (
        'name', 
        'start_date', 
        'end_date'
    )
    search_fields = (
        'name', 
        'status', 
        'start_date', 
        'end_date', 
        'create_date'
    )
    readonly_fields = ('create_date',)
    list_per_page = 25


admin.site.register(Offer, OfferAdmin)