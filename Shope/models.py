from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=225)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='Children', null=True, blank=True)
    orderId = models.IntegerField(null=True)

    class Meta:
        ordering = ('orderId', )
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    """продукт"""
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=225)
    description = models.TextField()
    price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField(null=True)
    color = models.CharField(max_length=125)
    size = models.FloatField()
    in_line = models.IntegerField()
    lines = models.IntegerField()
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


class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product/uploads/%Y/%m/%d/',)
    orderId = models.IntegerField(null=True)

    class Meta:
        ordering = ('orderId', )
        verbose_name = 'Изображение продукта'
        verbose_name_plural = 'Изображение продуктов'

    def __str__(self):
        return f'{self.product} {self.image}'
