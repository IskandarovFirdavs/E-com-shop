from django.contrib import admin

from products.models import CategoryModel, ColorModel, SizeModel, ProductModel, BannerModel

admin.site.register(BannerModel)


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


@admin.register(ColorModel)
class ColorModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


@admin.register(SizeModel)
class SizeModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_price', 'category', 'seller']
    search_fields = ['name', 'discount', 'category']
    list_filter = ['name', 'discount', 'category']
