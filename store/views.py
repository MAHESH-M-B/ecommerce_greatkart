from django.shortcuts import render
from rest_framework import viewsets

from .models import Product
from .serializer import ProductSerializer

# Create your views here.


class Productviewset(viewsets.ModelViewSet):
    serializer_class=ProductSerializer
    queryset=Product.objects.all()
