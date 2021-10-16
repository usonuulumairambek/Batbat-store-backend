from django.shortcuts import render
from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .serializers import (ProductSerializer, FavoriteProductSerializer,
                          CategorySerializer, ImageSerializer)
from .models import FavoritesProduct, Category, Product, Image


class ProductView(generics.GenericAPIView):
    serializer_class = ProductSerializer
    queryset = Product
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductFavouriteView(generics.RetrieveAPIView, generics.ListAPIView):
    serializer_class = FavoriteProductSerializer
    lookup_field = 'id'
    queryset = FavoritesProduct.objects.filter()


class ProductsFavouriteView(generics.ListAPIView):
    serializer_class = FavoriteProductSerializer
    queryset = FavoritesProduct.objects.filter()


# class CreatFavoriteProductView(generics.CreateAPIView):
#     serializer_class = FavoriteProductSerializer
#     queryset = FavoritesProduct.objects.filter()


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()
