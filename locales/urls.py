from django.urls import path,include

from locales.views import LocalesViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'',LocalesViewSet,basename='locales')

urlpatterns = [
    path('api/',include(router.urls)),

]