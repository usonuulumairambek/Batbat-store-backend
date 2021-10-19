from rest_framework import serializers

from .models import Product, Image, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'parent')


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('id', 'product', 'image')


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer
    updated = serializers.DateTimeField(read_only=True)
    created = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.discount = validated_data.get('discount', instance.discount)
        instance.color = validated_data.get('color', instance.color)
        instance.size = validated_data.get('size', instance.size)
        instance.in_line = validated_data.get('in_line', instance.in_line)
        instance.lines = validated_data.get('lines', instance.lines)
        instance.manufacturer_country = validated_data.get('manufacturer_country', instance.manufacturer_country)
        instance.available = validated_data.get('available', instance.available)
        instance.save()
        return instance

    class Meta:
        model = Product
        exclude = ('orderId',)


class ProductListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False)
    image = ImageSerializer(many=True, required=False)

    class Meta:
        model = Product
        exclude = ('orderId',)
