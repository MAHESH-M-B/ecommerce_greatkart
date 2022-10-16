from django.shortcuts import render
from rest_framework import viewsets

from .models import Products
from .serializer import ProductsSerializer

# Create your views here.


class Productsviewset(viewsets.ModelViewSet):
    serializer_class=ProductsSerializer
    queryset=Products.objects.all()