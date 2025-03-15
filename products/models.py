from django.db import models
from django.utils.translation import gettext_lazy as _

class CategoryModel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class SizeModel(models.Model):
    name = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Size'
        verbose_name_plural = 'Sizes'


class ColorModel(models.Model):
    name = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'


class BannerModel(models.Model):
    image = models.ImageField(upload_to='banners/', verbose_name=_('Image'))
    is_active = models.BooleanField(default=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.url

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'



class ProductModel(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("name"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("price"))
    discount = models.IntegerField(default=0, verbose_name=_("discount"))
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name='products',
                                 verbose_name=_("category"))
    size = models.ManyToManyField(SizeModel, related_name='products', verbose_name=_("size"))
    color = models.ManyToManyField(ColorModel, related_name='products', verbose_name=_("color"))
    short_description = models.TextField(verbose_name=_("short_description"))
    long_description = models.TextField(verbose_name=_("long_description"))
    image = models.ImageField(upload_to='products/', verbose_name=_("image"))
    is_available = models.BooleanField(default=True, verbose_name=_("is_available"))
    seller = models.ForeignKey('users.UserModel', on_delete=models.CASCADE, related_name='products',
                               verbose_name=_("seller"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created_at"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def get_price(self):
        if self.discount:
            return self.price - (self.price * self.discount / 100)
        return self.price

    def is_discounted(self):
        return self.discount > 0
