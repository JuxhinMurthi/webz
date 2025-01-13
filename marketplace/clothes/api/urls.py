from django.urls import path, include
from rest_framework import routers

from . import views


app_name = 'clothes'

router = routers.DefaultRouter()
router.register('clothes', views.GarmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
