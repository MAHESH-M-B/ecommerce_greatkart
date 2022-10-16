from django.contrib import admin

from .models import Product


# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    list_display=('product_name','price','stock','category','modified_date','is_available')
    prepopulated_fields={'slug':('product_name',)}


admin.site.register(Product,ProductsAdmin)