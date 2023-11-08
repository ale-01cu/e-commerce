from .views import CommentAPIViewset, ProductCommentsAPIView
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register('', CommentAPIViewset, basename='comments')

urlpatterns = [
    path('product/<int:pk>/', ProductCommentsAPIView.as_view(), name='product_comments_list')
    
] + router.urls
