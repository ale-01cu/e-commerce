from rest_framework.response import Response
from rest_framework.views import APIView
from apps.search_engine.serializers import SearchesListSerializer
from .serializers import CustomListsSerializer
from rest_framework import status, generics
from datetime import timedelta
from django.utils import timezone
from django.db.models import Q
from apps.product.serializers import ProductSerializerList

# Busquedas en Tendencia
class TrendingSearchesAPIView(APIView):
    def get(self, request):
        try:
            searchers = SearchesListSerializer.Meta.model.objects.all().order_by(
                '-number_searches')[:5]
            
            serializer = SearchesListSerializer(
                searchers, 
                context={'request': request}, 
                many=True
            )
            
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
            
        except Exception as e:
            print(e)
            return Response(
                {'error': 'Server internal error'}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
# Productos en Tendencia
class TrendingProductsAPIView(APIView):
    def get(self, request):
        try:
            products = ProductSerializerList.Meta.model.objects.filter(
                status=True,
                stock__gt=0
            ).order_by('-number_views')[:5]
            
            serializer = ProductSerializerList(
                products, 
                many=True
            )
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
            
        except Exception as e:
            print(e)
            return Response(
                {'error': 'Server internal error'}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            
# Productos mejor Valorados        
class TopRatedProductsAPIView(APIView):
    def get(self, request):
        try:
            products = ProductSerializerList.Meta.model.objects.filter(
                status=True,
                stock__gt=0
            )
            products = sorted(products, key=lambda p: p.rating, reverse=True)[:5]
            serializer = ProductSerializerList(
                products, 
                many=True
            )
            
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        except Exception as e:
            print(e)
            return Response(
                {'error': 'Server internal error'}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            
# Nuevos Productos de la semana 
class NewProductsAPIView(APIView):
    def get(self, request):
        try:
            current_time = timezone.now()
            one_week_ago = current_time - timedelta(weeks=1)

            products = ProductSerializerList.Meta.model.objects.filter(
                status=True,
                stock__gt=0,
                create_date__gte=one_week_ago
            ).order_by('-create_date')
            
            serializer = ProductSerializerList(
                products, 
                many=True
            )
            
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
            
        except Exception as e:
            print(e)
            return Response(
                {'error': 'Server internal error'}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            
# Mostrar Listas manuales y personalizadas   
class CustomListsAPIView(generics.ListAPIView):
    serializer_class = CustomListsSerializer
    now = timezone.now()
    queryset = CustomListsSerializer.Meta.model.objects.filter(
        Q(status=True) &
        Q(start_date__lte=now) &
        Q(end_date__gte=now)
    )