from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from ecomshop import settings
from django.conf.urls.i18n import i18n_patterns                                                                                                 


urlpatterns = []

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace='users')),
    path('contact/', include('contacts.urls', namespace='contact')),
    path('', include('products.urls', namespace='products')),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
