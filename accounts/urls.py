from django.urls import include, path
from rest_framework import routers

from .views import AccountViewset

router=routers.DefaultRouter()
router.register(r'Account', AccountViewset)


urlpatterns = [
   path('', include(router.urls)),
]
