#DRF
from rest_framework import serializers

# Models 
from items.models import Items

# Serializers
from locales.serializers import LocalesSerializer

class ItemsSerializer(serializers.ModelSerializer):

    data_local = LocalesSerializer(source='local',read_only=True)

    class Meta:

        model = Items
        fields = [
            'name',
            'price',
            'image',
            'local',
            'data_local',
            'fiabilidad_plus',
            'fiabilidad_minus',
            'created'
        ]
        extra_kwargs = {'local':{'write_only':True}}

