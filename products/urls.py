from django.urls import path

from products.views import (
    HomeListView,
    AboutTemplateView,
    ContactTemplateView,
    ShopTemplateView,
    ProductDetailView,
    LoginView,
    RegisterView
)

app_name = 'products'

urlpatterns = [
    path('', HomeListView.as_view(), name='list'),
    path('about/', AboutTemplateView.as_view(), name='about'),
    path('contact/', ContactTemplateView.as_view(), name='contact'),
    path('shop/', ShopTemplateView.as_view(), name='shop'),
    path('detail/<int:pk>', ProductDetailView.as_view(), name='detail'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
]
