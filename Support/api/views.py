from rest_framework import generics
from rest_framework.response import Response

from .tasks import send_change_status_email
from .viewsets.classes import CreateListRetrieveUpdateDestroyS, CreateListS, UpdateDestroyS

from .serializers import TicketCreateSerializer, \
    MessageSerializer, \
    MessageAdminSerializer, \
    TicketChangeStatusSerializer, \
    TicketListSerializer, \
    TicketDetailSerializer

from rest_framework.permissions import IsAuthenticated
from .models import Ticket, Message
from .viewsets.permissions import IsStaff, IsAuthorOrIsStaff, IsSuperUser, IsAuthorTicket


class TicketView(CreateListRetrieveUpdateDestroyS):
    """Ticket image"""

    queryset = Ticket.objects.all().order_by('-status')
    permission_classes = [IsStaff]
    serializer_class = TicketCreateSerializer
    permission_classes_by_action = {'create': [IsAuthenticated],
                                    'destroy': [IsSuperUser],
                                    'retrieve': [IsAuthorOrIsStaff],
                                    'list': [IsAuthenticated]}

    def get_serializer_class(self):
        if self.action == 'update' or self.action == 'partial_update':
            return TicketChangeStatusSerializer
        elif self.action == 'list':
            return TicketListSerializer
        elif self.action == 'retrieve':
            return TicketDetailSerializer
        else:
            return TicketCreateSerializer

    def list(self, request, *args, **kwargs):
        if request.user.is_staff:
            queryset = self.filter_queryset(self.get_queryset())
        else:
            queryset = Ticket.objects.all().filter(author=self.request.user).order_by('-status')
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        send_change_status_email.delay(serializer.instance.email, serializer.instance.status, serializer.validated_data)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CreateListMessageView(CreateListS):
    """"Create and review messages list"""

    queryset = Message.objects.all()
    permission_classes = [IsAuthorTicket]
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        ticket = Ticket.objects.get(id=self.kwargs['pk'])
        serializer.save(author=self.request.user, ticket=ticket)

    def get_queryset(self):
        ticket = self.kwargs['pk']
        return Message.objects.filter(ticket=ticket)


class UpdateMessageView(generics.UpdateAPIView):
    queryset = Message.objects.all()
    permission_classes = [IsSuperUser]
    serializer_class = MessageAdminSerializer


class DestroyMessageView(generics.DestroyAPIView):
    queryset = Message.objects.all()
    permission_classes = [IsSuperUser]
    serializer_class = MessageAdminSerializer
