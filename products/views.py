from django.views.generic import TemplateView, ListView, DetailView

from products.models import ProductModel, BannerModel


class HomeListView(ListView):
    queryset = ProductModel
    template_name = 'index.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['discounts'] = ProductModel.objects.order_by('-discount')[:3]
        context['banners'] = BannerModel.objects.filter(is_active=True)[:3]
        return context


class AboutTemplateView(TemplateView):
    template_name = 'about.html'


class ContactTemplateView(TemplateView):
    template_name = 'contact.html'


class ShopTemplateView(ListView):
    model = ProductModel
    template_name = 'shop.html'
    context_object_name = 'products'
    paginate_by = 9

    def get_queryset(self):
        qs = ProductModel.objects.all()

        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(name__icontains=q)

        return qs


class ProductDetailView(DetailView):
    model = ProductModel
    template_name = 'shop-single.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['related'] = self.object.category.products.exclude(pk=self.object.pk)[:4]
        return context
    


class LoginView(TemplateView):
    template_name = 'login.html'



class RegisterView(TemplateView):
    template_name = 'registration.html'
