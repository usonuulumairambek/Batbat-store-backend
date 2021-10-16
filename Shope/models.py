from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category = models.CharField(max_length=225)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='Children', null=True, blank=True)
    orderId = models.IntegerField(null=True)

    class Meta:
        ordering = ('orderId', )
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.category}'


color = (
    ('red', 'red'),
    ('black', 'black'),  # что лучше сделать так что бы все цвета были или что бы он сам через админку добавлял??
    ('orange', 'orange'),
)


class Product(models.Model):
    """продукт"""
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=225)
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=0)
    color = models.CharField(max_length=125)
    size = models.FloatField()
    seller = models.CharField(max_length=225)
    in_line = models.IntegerField()
    lines = models.IntegerField()
    discount = models.DecimalField(max_digits=20, decimal_places=0, null=True)
    cloth = models.CharField(max_length=64)
    manufacturer_country = models.CharField(max_length=32)
    orderId = models.IntegerField(null=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')


    class Meta:
        ordering = ('orderId', )
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.title}'


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/uploads/%Y/%m/%d/',)
    orderId = models.IntegerField(null=True)

    class Meta:
        ordering = ('orderId', )
        verbose_name = 'Изображение продукта'
        verbose_name_plural = 'Изображение продуктов'

    def __str__(self):
        return f'{self.product} {self.image}'


# class Sale(models.Model):
#     sale = models.DecimalField(max_digits=20, decimal_places=0)


class FavoritesProduct(models.Model):
    product = models.ManyToManyField(Product)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
