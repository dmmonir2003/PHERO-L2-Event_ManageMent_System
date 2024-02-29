from rest_framework.permissions import BasePermission


class IsAdminOrAuthenticatedAndIsAdmin(BasePermission):
    """
    Custom permission to allow only admin users to create service.
    """

    def has_permission(self, request, view):
        # Check if the user is authenticated and has an admin role
        return request.user and request.user.is_authenticated and request.user.role == 'admin'
