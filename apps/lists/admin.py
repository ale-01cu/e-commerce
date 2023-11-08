from django.contrib import admin
from .models import CustomsList, CustomsListItem

class CustomsListItemAdmin(admin.TabularInline):
    model = CustomsListItem
    extra = 1

class CustomsListAdmin(admin.ModelAdmin):
    inlines = [CustomsListItemAdmin]
    list_display = (
        'id',
        'name', 
        'status', 
        'start_date',
        'end_date',
        'create_date'
    )
    
    list_display_links = (
        'id',
        'name'
    )
    
    search_fields = ('name',)
    readonly_fields = ('create_date',)
    list_per_page = 10

admin.site.register(CustomsList, CustomsListAdmin)


# class MyAdminSite(admin.AdminSite):
#     def get_app_list(self, request):
#         app_list = super().get_app_list(request)
#         app_list += [
#             {
#                 "name": "My Custom App",
#                 "app_label": "my_test_app",
#                 # "app_url": "/admin/test_view",
#                 "models": [
#                     {
#                         "name": "tcptraceroute",
#                         "object_name": "tcptraceroute",
#                         "admin_url": "/admin/test_view",
#                         "view_only": True,
#                     }
#                 ],
#             }
#         ]
#         return app_list
