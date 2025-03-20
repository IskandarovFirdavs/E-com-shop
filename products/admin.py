from django.contrib import admin
from products.models import CategoryModel, ColorModel, SizeModel, ProductModel, BannerModel, ImageModel
from modeltranslation.translator import translator, TranslationOptions
from modeltranslation.admin import TranslationAdmin

class MyTranslationAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(CategoryModel)
class CategoryModelAdmin(MyTranslationAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    list_filter = ['name']


@admin.register(BannerModel)
class BannerModelAdmin(MyTranslationAdmin):
    list_display = ['id', 'description']
    search_fields = ['description']
    list_filter = ['description']


@admin.register(ColorModel)
class ColorModelAdmin(MyTranslationAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    list_filter = ['name']


@admin.register(SizeModel)
class SizeModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


class ImageModelAdmin(admin.TabularInline):
    model = ImageModel
    extra = 1
    
@admin.register(ProductModel)
class ProductModelAdmin(MyTranslationAdmin):
    list_display = ['id', 'name', 'get_price', 'category', 'seller']
    search_fields = ['name', 'discount', 'category']
    list_filter = ['name', 'discount', 'category']
    inlines = [ImageModelAdmin]
