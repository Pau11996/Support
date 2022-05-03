from django.contrib import admin
from .models import Ticket, Message


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'status', )


@admin.register(Message)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('text', 'author', 'ticket', 'comment_date', )