from rest_framework.response import Response
from rest_framework import status
from .models import Order
from .serializers import OrderSerializerDetail, OrderSerializerList, OrderSerializerCreate
from rest_framework.permissions import IsAuthenticated
from rest_framework import  viewsets
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action


class OrderAPIViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        try:
            user = request.user
            orders_queryset = Order.objects.filter(user=user)
            orders_serializer = OrderSerializerList(orders_queryset, many=True)
            
            return Response(
                orders_serializer.data,
                status=status.HTTP_200_OK
            )   
        except Exception as e:
            print(e)
            return Response(
                {'error': 'Something went wrong when retrieving order detail'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    
    def retrieve(self, request, pk=None):
        try:
            order_number = pk
            user = request.user
            order = Order.objects.filter(
                user=user, 
                order_number=order_number
            ).first()
            
            if order:
                order_serializer = OrderSerializerDetail(
                    order, 
                    context={'request': request}
                )
                
                return Response(
                    order_serializer.data,
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {'error': 'Order with this transaction ID does not exist'},
                    status=status.HTTP_404_NOT_FOUND
                )
        except Exception as e:
            print(e)
            return Response(
                {'error': 'Something went wrong when retrieving order detail'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
      
    def create(self, request):
        try:
            serializer = OrderSerializerCreate(
                data=request.data, 
                context={'request': request}
            )
            if serializer.is_valid():
                serializer.save()
                return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED
                )
                
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
            
        except Exception as e:
            print(e)
            return Response(
                {'error': 'Something went wrong when deleting order'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
          
                
    def update(self, request, pk=None):
        try:            
            order_number = pk
            user = request.user
            order_instance = get_object_or_404(
                Order, 
                order_number=order_number, 
                user=user
            )
            # Validar el estado de la orden
            if order_instance.status == 'cancelled':
                orderSerializer = OrderSerializerDetail(
                    instance=order_instance, 
                    data=request.data, 
                    context={'request': request}
                )
                if orderSerializer.is_valid():
                    orderSerializer.save()
                    return Response(
                        orderSerializer.data,
                        status=status.HTTP_200_OK
                    )
                    
                return Response(
                    {'error': 'invalid data'}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            return Response(
                {'error': 'Esta orden no puede ser actualizada.'}, 
                status=status.HTTP_401_UNAUTHORIZED
            )

        except Exception as e:
            print(e)
            return Response(
                {'error': 'Something went wrong when deleting order'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
        
    def destroy(self, request, pk=None):
        try:
            order_number = pk
            user = request.user
            order_instance = get_object_or_404(
                Order, 
                order_number=order_number, 
                user=user
            )
            # Validar el estado de la orden
            if order_instance.status == 'cancelled':
                order_instance.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            
            return Response(
                {'error': 'Esta orden no puede ser eliminada.'},
                status=status.HTTP_401_UNAUTHORIZED
            )
            
        except Exception as e:
            print(e)
            return Response(
                {'error': 'Something went wrong when deleting order'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            
            
    @action(methods=['get'], detail=True, url_path='cancel')
    def cancelOrder(self, request, order_number):
        try:
            user = request.user
            order_instance = get_object_or_404(
                Order, 
                order_number=order_number, 
                user=user
            )
            
            if order_instance.status == 'processed':
                return Response(
                {'error': 'You do not have access to delete the order because it is being processed, please! contact Customer Service.'},
                status=status.HTTP_401_UNAUTHORIZED
            )
            
            order_instance.status = 'cancelled'
            return Response(status=status.HTTP_204_NO_CONTENT)
            
        except Exception as e:
            print(e)
            return Response(
                {'error': 'Something went wrong when deleting order'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )