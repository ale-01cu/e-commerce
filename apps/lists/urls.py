from django.urls import path
from .views import (
    TrendingSearchesAPIView, TrendingProductsAPIView, 
    TopRatedProductsAPIView, NewProductsAPIView,
    CustomListsAPIView
)

urlpatterns = [
    path('treanding-searches/', TrendingSearchesAPIView.as_view(), name='trending-searches'),
    path('treanding-products/', TrendingProductsAPIView.as_view(), name='trending-products'),
    path('top-rated-products/', TopRatedProductsAPIView.as_view(), name='top-rated-products'),
    path('new-products/', NewProductsAPIView.as_view(), name='new-products'),
    path('custom-lists/', CustomListsAPIView.as_view(), name='custom-list'),
]