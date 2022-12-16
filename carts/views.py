from django.shortcuts import render

# Create your views here.


def carts(request):
    return render(request,'carts/carts.html')