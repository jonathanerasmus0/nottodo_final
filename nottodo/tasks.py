from django.core.mail import send_mail
from django.utils import timezone
from .models import NotToDo
from .utils import get_reminder_times
from celery import shared_task

@shared_task
def send_nottodo_notifications():
    now = timezone.now()
    time_threshold = now + timezone.timedelta(minutes=10)
    nottodos = NotToDo.objects.filter(
        scheduled_start_time__lte=time_threshold,
        scheduled_start_time__gte=now
    )
    for nottodo in nottodos:
        send_mail(
            'Not To Do Reminder',
            f'Remember not to do: {nottodo.title}',
            'joesaudi@hotmail.com',
            [nottodo.user.email],
            fail_silently=False,
        )

@shared_task
def check_and_send_reminders():
    now = timezone.now()
    nottodos = NotToDo.objects.filter(scheduled_start_time__gte=now)

    for nottodo in nottodos:
        reminder_times = get_reminder_times(nottodo)
        for reminder_time in reminder_times:
            if now >= reminder_time and now <= (reminder_time + timezone.timedelta(minutes=10)):
                send_mail(
                    'Not To Do Reminder',
                    f'Remember not to do: {nottodo.title}',
                    'joesaudi@hotmail.com',
                    [nottodo.user.email],
                    fail_silently=False,
                )
