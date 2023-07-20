from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'purchase_status', 'purchase_date')
    search_fields = ('name', 'category')


admin.site.register(Product, ProductAdmin)
