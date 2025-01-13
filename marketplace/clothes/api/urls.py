from django.urls import path, include
from rest_framework import routers

from . import views


app_name = 'clothes'

router = routers.DefaultRouter()
router.register('clothes', views.GarmentViewSet)

urlpatterns = [
    path('clothes/publish/', views.GarmentPublishView.as_view(), name='garment_publish'),
    path('clothes/<pk>/update/', views.GarmentUpdateView.as_view(), name='garment_update'),
    path('clothes/<pk>/delete/', views.GarmentDeleteView.as_view(), name='garment_delete'),
    path('', include(router.urls)),
]
