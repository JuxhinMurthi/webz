from rest_framework import serializers

from clothes.models import Garment


class GarmentSerializer(serializers.ModelSerializer):
    """ Garment Serializer """
    publisher = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Garment
        fields = [
            'id',
            'publisher',
            'description',
            'price',
            'size',
            'type'
        ]
