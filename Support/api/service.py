from collections import OrderedDict

from django.core.mail import send_mail


def change_status_email(user_email: str, from_ticket_status: str, to_ticket_status: OrderedDict):
    """Email sending function"""

    to_ticket_status_obj = list(to_ticket_status.items())
    send_mail(
        'Hello dear user',
        f'We notify you about the ticket status change from {from_ticket_status} to {to_ticket_status_obj[0][1]}',
        'nomerfill@gmail.com',
        [user_email],
        fail_silently=False
        )
