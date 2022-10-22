from django.urls import include, path
from rest_framework import routers

from store import views
from .views import Productviewset

router = routers.DefaultRouter()
router.register(r'Product', Productviewset)


urlpatterns = [
    path('store/', views.store, name='store'),
    path('api/product_api/', include(router.urls)),
    path('store/<slug:category_slug>/',views.store, name='product_by_category'),   
]


