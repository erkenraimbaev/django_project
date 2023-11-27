from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.views import home, contacts, product

urlpatterns = [
    path('', home),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', product, name='product')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
