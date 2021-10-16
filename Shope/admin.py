
from django.contrib import admin

# Register your models here.
from Shope.models import Category, Product, Image, FavoritesProduct

from adminsortable2.admin import SortableAdminMixin


@admin.register(Category)
class CategoryAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('category', 'parent')


@admin.register(Product)
class ProductAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'price', 'color', 'seller')


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('product', 'image')


@admin.register(FavoritesProduct)
class ProductFavorite(admin.ModelAdmin):
    list_display = ('user', )
