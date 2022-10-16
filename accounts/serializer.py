from rest_framework import serializers

from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=Account
        # fields=('first_name','last_name','username','email','phone_number','date_joined','last_login','is_admin','is_staff','is_active','is_superadmin')
        fields='__all__'