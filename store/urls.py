from django.urls import include, path
from rest_framework import routers

from .views import Productsviewset

router=routers.DefaultRouter()
router.register(r'Products',Productsviewset)


urlpatterns = [
   path('', include(router.urls)),
]
