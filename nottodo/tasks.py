from django.core.mail import send_mail
from django.utils import timezone
from .models import NotToDo
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