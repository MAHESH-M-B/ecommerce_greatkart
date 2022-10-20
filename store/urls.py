from django.urls import include, path
from rest_framework import routers

from . import views
from .views import Productviewset

router = routers.DefaultRouter()
router.register(r'Product', Productviewset)


urlpatterns = [
    # path('store/', views.store, name='store'),
    path('product_api/', include(router.urls)),
    
]
