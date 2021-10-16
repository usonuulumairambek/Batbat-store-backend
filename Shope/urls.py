from django.urls import path, include
from rest_framework import routers

from .views import CategoryViewSet, ImageViewSet


router = routers.SimpleRouter()
router.register('category', CategoryViewSet)
router.register('image', ImageViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
