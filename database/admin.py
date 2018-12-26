from django.contrib import admin
from .models import *

admin.site.site_header = 'E Agora DB'

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type')


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Selling)
class SellingAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'store_id', 'price')

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'store_id', 'client')

@admin.register(Has)
class HasAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'order_id', 'quantity')
