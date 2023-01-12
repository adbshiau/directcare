from django.contrib import admin
from .models import Item, Order

admin.site.site_header = 'DC Inventory Admin'

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity')
    list_filter = ['category']

# Register your models here.
admin.site.register(Item, ItemAdmin)
admin.site.register(Order)