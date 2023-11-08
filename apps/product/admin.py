from django.contrib import admin
from apps.product import models
from .forms import ProductForm


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "photo",
        "price",
        "stock",
        "discount_price",
        "create_date",
    )
    list_display_links = (
        "id",
        "name",
        "photo",
    )
    search_fields = ("name", "brand", "stock", "keywords", "create_date")
    form = ProductForm
    readonly_fields = ("create_date",)
    list_per_page = 25


class MeasureUnitAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "symbol")
    list_display_links = ("name", "symbol")
    search_fields = ("name", "symbol")
    list_per_page = 25


class BrandAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    list_per_page = 25


class ImageAdmin(admin.ModelAdmin):
    list_display = ("id", "image")
    list_display_links = ("id", "image")
    search_fields = ("image",)
    list_per_page = 25


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Measure_unit, MeasureUnitAdmin)
admin.site.register(models.Image, ImageAdmin)
admin.site.register(models.Brand, BrandAdmin)
