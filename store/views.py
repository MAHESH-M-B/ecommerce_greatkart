from django.shortcuts import render
from rest_framework import viewsets

from .models import Product
from .serializer import ProductSerializer

# Create your views here.

class store_import():
    def store(request):
        products=Product.objects.all().filter(is_available=True)
        products_count=products.count()
        context={
            'products':products,
            'products_count':products_count,
        }
        return render(request,'store/store.html',context)
    


class Productviewset(viewsets.ModelViewSet):
    serializer_class=ProductSerializer
    queryset=Product.objects.all()
