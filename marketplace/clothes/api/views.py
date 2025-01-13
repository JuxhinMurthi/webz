from rest_framework import generics
from rest_framework import viewsets

from clothes.api.serializers import GarmentSerializer
from clothes.models import Garment
from clothes.api.pagination import StandardPagination


class GarmentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Garment.objects.prefetch_related('publisher')
    serializer_class = GarmentSerializer
    pagination_class = StandardPagination
