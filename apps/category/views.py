from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CategorySerializer
from core.permissions import IsAdminOrReadOnly

class CategoryAPIView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
    
    def get_queryset(self):
        return self.get_serializer_class().Meta.model.objects.filter(status=True)