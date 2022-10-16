from rest_framework import serializers

from .models import Products


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields=('product_name','slug','description','price','images','stock','is_available','category','created_date','modified_date')