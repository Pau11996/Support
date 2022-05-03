from rest_framework.permissions import BasePermission

from ..models import Ticket


class IsStaff(BasePermission):
    """Support"""
    def has_permission(self, request, view):
        return request.user and request.user.is_staff


class IsAuthorOrIsStaff(BasePermission):
    """Is author or Support"""
    def has_permission(self, request, view):
        return request.user or request.user.is_staff

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user or request.user.is_staff


class IsSuperUser(BasePermission):
    """Superuser"""
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_superuser


class IsAuthorTicket(BasePermission):
    """Ticket Author or Support"""

    def has_permission(self, request, view):
        ticket = Ticket.objects.get(id=request.resolver_match.kwargs.get('pk'))
        return ticket.author == request.user or request.user.is_staff

