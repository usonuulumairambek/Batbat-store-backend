from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Product, Image, Category


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ('category', 'parent')


class ProductSerializer(ModelSerializer):
    category = CategorySerializer

    class Meta:
        model = Product
        fields = ('id', 'category', 'title', 'description', 'price', 'color',
                  'size', 'seller', 'in_line', 'lines', 'discount', 'favorite')


class FavoriteProductSerializer(ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Image
        fields = ('id', 'product', 'user_id')


class ImageSerializer(ModelSerializer):

    class Meta:
        model = Image
        fields = ('id', 'product', 'image')
