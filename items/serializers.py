#DRF
from rest_framework import serializers

# Models 
from items.models import Items

# Serializers
from locales.serializers import LocalesSerializer

class ItemsSerializer(serializers.ModelSerializer):

    data_locales = LocalesSerializer(source='locales',read_only=True,many=True)

    class Meta:

        model = Items
        fields = [
            'name',
            'price',
            'image',
            'locales',
            'data_locales',
            'fiabilidad_plus',
            'fiabilidad_minus',
            'created'
        ]
        extra_kwargs = {'locales':{'write_only':True}}

