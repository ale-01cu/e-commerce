from django.contrib import admin
from .models import Order, OrderItem
    
class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    extra = 1
    

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemAdmin]
    list_display = ('id', 'order_number', 'amount', 'order_status')
    list_display_links = ('id', 'order_number', )
    list_filter = ('order_status',)
    list_editable = ('order_status', )
    readonly_fields = ('order_number', 'amount', 'total_price')
    list_per_page = 25

    # def has_add_permission(self, request):
    #     return False


admin.site.register(Order, OrderAdmin)