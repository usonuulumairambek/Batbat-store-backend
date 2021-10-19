from django.urls import path, include
from rest_framework import routers

from .views import CategoryViewSet, ImageViewSet, ProductViewSet


router = routers.SimpleRouter()
router.register('category', CategoryViewSet)
router.register('image', ImageViewSet)
router.register('product', ProductViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
