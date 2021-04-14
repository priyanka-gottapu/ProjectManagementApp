from django.contrib import admin
from .models import Books,Tasks,TaskList
admin.site.register(Books)
admin.site.register(Tasks)
admin.site.register(TaskList)
# Register your models here.