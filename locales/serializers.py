# DRF
from rest_framework import serializers

# Models
from locales.models import Local

class LocalesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Local
        fields = '__all__'