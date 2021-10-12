from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=225)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='Children', null=True, blank=True)

    def __str__(self):
        return f'{self.category}'

color = (
    ('red', 'red'),
    ('black', 'black'), # что лучше сделать так что бы все цвета были или что бы он сам через админку добавлял??
    ('orange', 'orange'),
)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=225)
    description = models.TextField()
    price = models.FloatField()
    color = models.CharField(max_length=125)
    size = models.FloatField()
    seller = models.CharField(max_length=225)
    in_line = models.IntegerField()
    lines = models.IntegerField()

    def __str__(self):
        return f'{self.title}'


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/uploads/%Y/%m/%d/',)

    def __str__(self):
        return f'{self.product} {self.image}'