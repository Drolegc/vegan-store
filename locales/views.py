# DRF
from rest_framework import viewsets
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
# Model
from locales.models import Local

# Serializers
from locales.serializers import LocalesSerializer

# Create your views here.

class LocalesViewSet(viewsets.ModelViewSet):

    queryset = Local.objects.all()
    serializer_class = LocalesSerializer
    filter_backends = (SearchFilter,DjangoFilterBackend,OrderingFilter)
