from django.urls import path
from .views import HIstoryAPIView

urlpatterns = [
    path('', HIstoryAPIView.as_view(), name='user_history-detail')
]