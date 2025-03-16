from products.models import CategoryModel, ColorModel, SizeModel, ProductModel, BannerModel
from modeltranslation.translator import register, TranslationOptions


@register(CategoryModel)
class CategoryModelTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(ColorModel)
class ColorModelTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(ProductModel)
class ProductModelTranslationOptions(TranslationOptions):
    fields = ("name", "long_description", "short_description",)


@register(BannerModel)
class BannerModelTranslationOptions(TranslationOptions):
    fields = ("description",)
