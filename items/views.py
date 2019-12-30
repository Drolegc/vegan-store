# DRF
from rest_framework import viewsets
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# Model
from items.models import Items

# Serializers
from items.serializers import ItemsSerializer

# Create your views here.

class ItemsViewSet(viewsets.ModelViewSet):

    queryset = Items.objects.all()
    serializer_class = ItemsSerializer
    filter_backends = (SearchFilter,DjangoFilterBackend,OrderingFilter)

