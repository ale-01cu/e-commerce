from .serializers import CommentsSerializerDetail, CommentsListSerializer
from rest_framework import status, viewsets, views
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .pagination import CommentsPagination
from apps.product.models import Product
from .permissions import CommentIsCreatedByUser, UserHasNoComment

# Vista encargada de manejar los comentarios por los usuarios
class CommentAPIViewset(viewsets.ModelViewSet):
    pagination_class = CommentsPagination
    serializer_class = CommentsSerializerDetail
    permission_classes = [
        IsAuthenticatedOrReadOnly, 
        CommentIsCreatedByUser,
        UserHasNoComment
    ]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self, pk=None):
        if pk: 
            return CommentsListSerializer.Meta.model.objects.filter(
                pk=pk,
                status=True).first()
        return CommentsListSerializer.Meta.model.objects.filter(status=True)
    
        
        
# Devuelve los comentarios de un producto paginados
class ProductCommentsAPIView(views.APIView):
    def get_serializer_class(self):
        return CommentsListSerializer 
    
    def get_product(self, pk=None):
        if pk:
            return Product.objects.filter(
                pk=pk,
                status=True, 
                stock__gt=0
            )
        return None
    
    def pagination_class(self):
        return CommentsPagination

    def get(self, request, pk=None):
        try:
            product = self.get_queryset(pk)
            comment_queryset = product.comments.filter(status=True)
            paginator = self.pagination_class()()
            
            paginated_comments = paginator.paginate_queryset(
                comment_queryset, 
                request, 
                view=self
            )
            
            comment_serializer = self.get_serializer_class()
            comment_serializer = comment_serializer(
                paginated_comments, 
                many=True
            )
            response = paginator.get_paginated_response(
                comment_serializer.data).data
            
            return Response({
                'next': response['next'],
                'results': response['results']
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
            print(e)
            return Response(
                {'error': 'Server internal error'}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )