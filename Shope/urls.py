from django.urls import path, include
from rest_framework import routers

from . import views
from .views import CategoryViewSet, ImageViewSet, ProductViewSet


router = routers.SimpleRouter()
router.register('category', CategoryViewSet)
router.register('image', ImageViewSet)
router.register('product', ProductViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('favorite-product/<int:pk>/', views.AddFavoriteProductView.as_view()), # add favorite product
    path('favoirte-products/', views.GetFavoriteProductView.as_view()), # receive products
]
