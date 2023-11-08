from rest_framework.permissions import BasePermission, IsAuthenticated
from .models import Comments

class CommentIsCreatedByUser(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'DELETE' or request.method == 'PUT' or request.method == 'PATCH':
            user = request.user
            params = view.kwargs
            
            if 'pk' in params.keys() and user.is_authenticated:
                comment = Comments.objects.filter(
                    pk=params['pk'],
                    user=user,
                    status=True
                ).first()
                
                if not comment:
                    return False
        
        return super().has_permission(request, view)
    
    
class UserHasNoComment(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            user = request.user
            product_id = None
            
            if 'product' in request.data.keys():
                product_id = request.data['product']
                                
            if product_id:
                comment = Comments.objects.filter(
                    user=user,
                    product_id=product_id
                ).first()
                
                if comment:
                    return False
            
        return super().has_permission(request, view)