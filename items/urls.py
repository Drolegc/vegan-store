from django.urls import path,include

from items.views import ItemsViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'',ItemsViewSet,basename='items')

urlpatterns = [
    path('api/',include(router.urls)),
]