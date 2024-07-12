import datetime
from django.utils import timezone
from django.core.mail import send_mail
from .models import NotToDo

def get_reminder_times(nottodo):
    reminder_times = []
    start_time = nottodo.scheduled_start_time - datetime.timedelta(minutes=10)
    end_time = nottodo.scheduled_end_time
    current_time = start_time

    if nottodo.repeat == 'Daily':
        delta = datetime.timedelta(days=1)
    elif nottodo.repeat == 'Weekly':
        delta = datetime.timedelta(weeks=1)
    elif nottodo.repeat == 'Monthly':
        delta = datetime.timedelta(weeks=4)  # Approximation for simplicity

    while current_time <= end_time:
        reminder_times.append(current_time)
        current_time += delta

    return reminder_times

def send_reminder_email(user, nottodo):
    subject = f"Reminder: {nottodo.title}"
    message = f"This is a reminder for your NotToDo item '{nottodo.title}' starting at {nottodo.scheduled_start_time}."
    send_mail(subject, message, 'noreply@example.com', [user.email])
