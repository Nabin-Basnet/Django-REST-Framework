from django.contrib import admin
from .models import person,student

# Register your models here.
admin.site.register([person,student])