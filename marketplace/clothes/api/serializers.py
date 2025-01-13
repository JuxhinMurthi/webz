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

    def __init__(self, *args, **kwargs):
        """ Make description and price fields optional only for updates """
        super().__init__(*args, **kwargs)
        if self.instance:  # Only for updates
            self.fields['description'].required = False
            self.fields['price'].required = False
