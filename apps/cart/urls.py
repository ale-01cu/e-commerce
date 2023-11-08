from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    CartAPIViewSet,
    GetTotalView, 
    GetItemTotalView, 
    EmptyCartView, 
    SynchCartView
)

routers = DefaultRouter()
routers.register('', CartAPIViewSet, basename='cart-viewset')


urlpatterns = [
    path('totalCost/', GetTotalView.as_view(), name='get-item-total-cost-cart'),
    path('total-items/', GetItemTotalView.as_view(), name='get-all-cart'),
    path('empty/', EmptyCartView.as_view(), name='empty-cart'),
    path('synch/', SynchCartView.as_view(), name='synch-cart'),
] + routers.urls