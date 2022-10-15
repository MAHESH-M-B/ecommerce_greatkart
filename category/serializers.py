
from rest_framework import serializers

from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=('category_name','slug','description','cat_image')

