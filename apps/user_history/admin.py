from django.contrib import admin
from .models import History, HistoryItem

class HistoryItemAdmin(admin.TabularInline):
    model = HistoryItem
    extra = 0
    can_delete = True
    

class HistoryAdmin(admin.ModelAdmin):
    inlines = [HistoryItemAdmin]
    list_display = ('id', 'user')
    list_display_links = ('id', 'user')
    search_fields = ('user', )
    list_per_page = 25
    
    
admin.site.register(History, HistoryAdmin)