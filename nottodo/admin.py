from django.contrib import admin
from .models import NotToDo, SharedNotToDo, Comment

admin.site.register(NotToDo)
admin.site.register(SharedNotToDo)
admin.site.register(Comment)

