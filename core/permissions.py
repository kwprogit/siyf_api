from rest_framework.permissions import BasePermission, IsAuthenticated


IsAuth = IsAuthenticated

class IsSuper(BasePermission):
    message = "You are not superuser"
    def has_permission(self, request, view):
        return request.user.is_superuser
    
