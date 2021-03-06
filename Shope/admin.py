from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin

from Shope.models import Category, Product, Images


@admin.register(Category)
class CategoryAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'parent')


@admin.register(Product)
class ProductAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'price', 'color')


@admin.register(Images)
class ImagesAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('product', 'image')
