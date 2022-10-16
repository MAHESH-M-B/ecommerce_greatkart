from django.shortcuts import render
from rest_framework import viewsets

from .models import Account
from .serializer import AccountSerializer

# Create your views here.

class AccountViewset(viewsets.ModelViewSet):
    serializer_class=AccountSerializer
    queryset=Account.objects.all()