
from django.urls import path
from .views import ProductDescriptionAPIView, ImageContentView

urlpatterns = [
    path('generate-product-description/', ProductDescriptionAPIView.as_view(), name='generate-product-description'),
    path('image-keyword/', ImageContentView.as_view(), name='image-upload'),
]
