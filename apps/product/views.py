from .serializers import ProductSerializerDetail, ProductSerializerList
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from .pagination import ProductsPagination

# Vista para listar los productos
class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializerList
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']
    
    def get_queryset(self):
        return self.get_serializer_class().Meta.model.objects.filter(
            stock__gt=0, 
            status=True
        )

# Vista para mostrar el detalle de un producto
class ProductRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ProductSerializerDetail
    
    def get_queryset(self, pk=None):
        if pk:
            return self.get_serializer_class().Meta.model.objects.filter(
                stock__gt=0, 
                status=True,
                pk=pk
            )
        
        return self.get_serializer_class().Meta.model.objects.filter(
            stock__gt=0, 
            status=True
        )