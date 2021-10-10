from django.contrib import admin
from .models import products

# Register your models here.
class ProductssAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'Category', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}

admin.site.register(products, ProductssAdmin)