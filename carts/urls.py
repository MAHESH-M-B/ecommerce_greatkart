from django.urls import path
from carts import views
urlpatterns=[
    path('carts/',views.carts,name='carts')
]