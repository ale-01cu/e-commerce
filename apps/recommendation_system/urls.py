from django.urls import path
from .views import RelatedProductAPIView

urlpatterns = [
    path('related-products/<int:product_id>/', RelatedProductAPIView.as_view(), name='related_products_list')
]