from Support.celery import app

from .service import change_status_email


@app.task
def send_change_status_email(user_email, from_ticket_status, to_ticket_status):
    change_status_email(user_email, from_ticket_status, to_ticket_status)