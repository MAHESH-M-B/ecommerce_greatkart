from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        # fields=('product_name','slug','description','price','images','stock','is_available','category','created_date','modified_date')
        fields='__all__'