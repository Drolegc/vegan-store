# DRF
from rest_framework import viewsets

# Model
from items.models import Items

# Serializers
from items.serializers import ItemsSerializer

# Create your views here.

class ItemsViewSet(viewsets.ModelViewSet):

    queryset = Items.objects.all()
    serializer_class = ItemsSerializer
    lookup_field = 'name'
