# nottodo/tasks.py
from django.core.mail import send_mail
from django.utils import timezone
from .models import NotToDo

def send_nottodo_notifications():
    now = timezone.now() + timezone.timedelta(minutes=30)
    nottodos = NotToDo.objects.filter(scheduled_time__lte=now, scheduled_time__gte=timezone.now())
    for nottodo in nottodos:
        send_mail(
            'Not To Do Reminder',
            f'Remember not to do: {nottodo.title}',
            'joesaudi@hotmail.com',
            [nottodo.user.email],
            fail_silently=False,
        )
