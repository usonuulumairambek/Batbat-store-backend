from django.shortcuts import render
from rest_framework import generics, status
from .serializers import ProductSerializer, FavoriteProductSerializer
from .models import Product
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from Shope.models import FavoritesProduct


class ProductView(APIView):
    serializer_class = ProductSerializer
    
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


