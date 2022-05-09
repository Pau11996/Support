from rest_framework.permissions import BasePermission

from ..models import Ticket


class IsStaff(BasePermission):
    """Support access."""
    def has_permission(self, request: object, view: object):
        return request.user and request.user.is_staff


class IsAuthorOrIsStaff(BasePermission):
    """Access for author or support."""
    def has_permission(self, request: object, view: object):
        return request.user or request.user.is_staff

    def has_object_permission(self, request: object, view: object, obj: object):
        return obj.author == request.user or request.user.is_staff


class IsSuperUser(BasePermission):
    """Access for superuser."""
    def has_permission(self, request: object, view: object):
        return request.user and request.user.is_superuser

    def has_object_permission(self, request: object, view: object, obj: object):
        return request.user and request.user.is_superuser


class IsAuthorTicket(BasePermission):
    """The list of messages is available only for the tickets author or support."""
    def has_permission(self, request: object, view: object):
        ticket = Ticket.objects.get(id=request.resolver_match.kwargs.get('pk'))
        return ticket.author == request.user or request.user.is_staff

