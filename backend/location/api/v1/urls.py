from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    TaskerLocationViewSet,
    MapLocationViewSet,
    CustomerLocationViewSet,
    TaskLocationViewSet,
)

router = DefaultRouter()
router.register("tasklocation", TaskLocationViewSet)
router.register("taskerlocation", TaskerLocationViewSet)
router.register("customerlocation", CustomerLocationViewSet)
router.register("maplocation", MapLocationViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
