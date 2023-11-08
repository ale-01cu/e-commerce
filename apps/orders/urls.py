from django.urls import path
from .views import OrderAPIViewSet
from rest_framework.routers import DefaultRouter

routers = DefaultRouter()
routers.register(r'', OrderAPIViewSet, basename='orders')

urlpatterns = routers.urls