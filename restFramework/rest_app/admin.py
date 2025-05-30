from django.contrib import admin
from .models import person,student,teacher,Employee

# Register your models here.
admin.site.register([person,student,teacher,Employee])