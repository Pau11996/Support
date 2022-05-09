from rest_framework import serializers

from .models import Ticket, Message


class TicketCreateSerializer(serializers.ModelSerializer):
    """Serialize all tickets."""
    class Meta:
        model = Ticket
        fields = ('first_name', 'last_name', 'email', 'phone', 'address', 'title', 'text', )


class TicketDetailSerializer(serializers.ModelSerializer):
    """Serialize all tickets for detail view."""
    author = serializers.SlugRelatedField(slug_field='username', read_only='True')

    class Meta:
        model = Ticket
        fields = ('author', 'status', 'first_name', 'last_name', 'email', 'phone', 'address', 'title', 'text', )


class TicketChangeStatusSerializer(serializers.ModelSerializer):
    """Serialize all tickets for change status."""
    class Meta:
        model = Ticket
        fields = '__all__'
        read_only_fields = \
            ('id', 'author', 'first_name', 'last_name', 'email', 'phone', 'address', 'title', 'text', 'ticket_date', )


class TicketListSerializer(serializers.ModelSerializer):
    """Serialize tickets list."""
    class Meta:
        model = Ticket
        fields = ('title', 'status', 'ticket_date', 'id', )
        read_only_fields = ('__all__', )


class MessageSerializer(serializers.ModelSerializer):
    """Serialize messages."""
    author = serializers.SlugRelatedField(slug_field='username', read_only='True')

    class Meta:
        model = Message
        fields = ('author', 'text', 'comment_date', )
        read_only_fields = ('__all__', )


class MessageAdminSerializer(serializers.ModelSerializer):
    """Serialize messages for Admin user."""
    class Meta:
        model = Message
        fields = '__all__'
