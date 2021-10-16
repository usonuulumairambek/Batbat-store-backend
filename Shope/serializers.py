from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from Shope.models import Product, Image
from django.contrib.auth.models import User


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'category', 'title', 'description', 'price', 'color',
                  'size', 'seller', 'in_line', 'lines', 'discount', 'favorite',
                  )


class FavoriteProductSerializer(ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Image
        fields = ('id', 'product', 'user_id')