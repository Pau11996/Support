from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models


class Ticket(models.Model):
    """Ticket model"""

    STATUS_IN_PROGRESS = 'Ticket in progress'
    STATUS_FROZEN = 'Ticket frozen'
    STATUS_COMPLETED = 'Ticket completed'

    STATUS_CHOICES = (
        (STATUS_IN_PROGRESS, 'Ticket in progress'),
        (STATUS_FROZEN, 'Ticket frozen'),
        (STATUS_COMPLETED, 'Ticket completed'),
    )

    first_name = models.CharField(max_length=255, verbose_name='Name')
    last_name = models.CharField(max_length=255, verbose_name='Last name')
    email = models.EmailField(max_length=50, verbose_name='Email')
    author = models.ForeignKey(User, verbose_name='author', on_delete=models.CASCADE, null=True, blank=True)
    phone = models.CharField(max_length=255, verbose_name='Phone', validators=[RegexValidator(r'^\+[0-9]{12}$')])
    address = models.CharField(max_length=1024, verbose_name='Address', null=True, blank=True)
    title = models.CharField(max_length=100, verbose_name='Tickets title')
    text = models.TextField(verbose_name='Ticket text')
    status = models.CharField(max_length=100,
                              verbose_name='Ticket status',
                              choices=STATUS_CHOICES,
                              default=STATUS_IN_PROGRESS)
    ticket_date = models.DateTimeField(verbose_name='Date ticket created', auto_now=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'


class Message(models.Model):
    """Message model"""

    text = models.TextField(verbose_name='Message text')
    author = models.ForeignKey(User, verbose_name='Message author', on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket,
                               verbose_name='Ticket message',
                               on_delete=models.CASCADE,
                               related_name='Messages',
                               null=True, blank=True)
    comment_date = models.DateTimeField(verbose_name='Date message created', auto_now=True)

    def __str__(self):
        return str(self.text)

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
