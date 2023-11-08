from rest_framework.permissions import BasePermission, IsAuthenticated
    
class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        
        is_Authenticated = IsAuthenticated().has_permission(request, view)
        staff_permissions = bool(request.user and (request.user.is_staff or request.user.is_superuser))
        return bool(is_Authenticated and staff_permissions)
        