from functools import partial

from rest_framework import (
    generics,
    viewsets,
    views,
    filters,
    response,
    permissions,
    status
)

from clothes.api.serializers import GarmentSerializer
from clothes.models import Garment
from clothes.api.pagination import StandardPagination
from rest_framework.exceptions import PermissionDenied


class GarmentViewSet(viewsets.ReadOnlyModelViewSet):
    """ Garment list and detail views for read-only purposes. No authentication required.  """
    queryset = Garment.objects.prefetch_related('publisher')
    serializer_class = GarmentSerializer
    pagination_class = StandardPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['description', 'price', 'type', 'size', 'publisher__username']


class GarmentPublishView(views.APIView):
    """ Publish a garment. Authentication required. """

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = GarmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(publisher=request.user)
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GarmentUpdateView(generics.UpdateAPIView):
    """ Update a garment. Authentication and garment ownership required. """

    queryset = Garment.objects.all()
    serializer_class = GarmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        garment = self.get_object()
        if garment.publisher != self.request.user:
            raise PermissionDenied('You are not allowed to update this record.')

        serializer.save()


class GarmentDeleteView(generics.DestroyAPIView):
    """ Delete a garment. Authentication and garment ownership required. """

    queryset = Garment.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        if instance.publisher != self.request.user:
            raise PermissionDenied('You are not allowed to delete this record.')

        super().perform_destroy(instance)
