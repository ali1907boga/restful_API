from rest_framework import permissions
from rest_framework.permissions import BasePermission,SAFE_METHODS


class IsSuperUser(BasePermission):
    """
    Allows access only to admin superusers.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)

class IsStaffOrReadOnly(BasePermission):

    def has_permission(self, request, view):

        if request.method in SAFE_METHODS:
            return True
        return bool(
            request.is_staff and request.user.is_authenticated
            or
            request.user.is_superuser and request.user.is_authenticated
        )





