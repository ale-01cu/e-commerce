from django.urls import path
from .views import ProductRetrieveAPIView, ProductListAPIView

urlpatterns = [
    path('', ProductListAPIView.as_view(), name='product-list'),
    path('<int:pk>/', ProductRetrieveAPIView.as_view(), name='product-detail'),
]