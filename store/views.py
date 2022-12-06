from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets

from category.models import Category

from .models import Product
from .serializer import ProductSerializer
# Create your views here.

def store(request, category_slug=None):
    categories = None
    products = None
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        products_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        products_count = products.count()
    
    context = {
        'products': products,
        'products_count': products_count,
    }
    return render(request, 'store/store.html', context)


def product_detail(request,category_slug,product_slug):
    try:
        single_product=Product.objects.get(category__slug=category_slug,slug=product_slug)
    except Exception:
        raise Exception
    context={
        'single_product':single_product
    }
    return render(request,'store/product_detail.html',context)

class Productviewset(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
