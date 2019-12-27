# DRF
from rest_framework import viewsets

# Model
from locales.models import Local

# Serializers
from locales.serializers import LocalesSerializer

# Create your views here.

class LocalesViewSet(viewsets.ModelViewSet):

    queryset = Local.objects.all()
    serializer_class = LocalesSerializer
    lookup_field = 'name'
