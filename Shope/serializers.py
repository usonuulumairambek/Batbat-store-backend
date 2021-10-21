from rest_framework import serializers

from .models import Product, Images, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'parent')


class ImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Images
        fields = ('id', 'product', 'image')


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer
    images = ImagesSerializer(many=True, required=False)
    updated = serializers.DateTimeField(read_only=True)
    created = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        images = self.context.get('request').FILES
        product = Product.objects.create(
            category=validated_data.get('category'),
            title=validated_data.get('title'),
            description=validated_data.get('description'),
            price=validated_data.get('price'),
            discount=validated_data.get('discount'),
            color=validated_data.get('color'),
            size=validated_data.get('size'),
            in_line=validated_data.get('in_line'),
            lines=validated_data.get('lines'),
            manufacturer_country=validated_data.get('manufacturer_country'),
            available=validated_data.get('available'),
        )
        if images:
            for image in images.values():
                Images.objects.create(product=product, image=image)
        return product

    def update(self, instance, validated_data):
        image = self.context.get('request').FILES
        Images.objects.create(product_id=instance.id, image=image.get('images'))

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
    """Этот сериализатор используетя только для get list и get detail запросов
    За все другие запросы отвечает ProductSerializer"""
    category = CategorySerializer(many=False)
    images = ImagesSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = '__all__'
