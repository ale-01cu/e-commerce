from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CategoryAPIView

router = DefaultRouter()
router.register(f'', CategoryAPIView, basename='categorys')

urlpatterns = router.urls