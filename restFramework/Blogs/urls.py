from django.urls import path,include
from .views import blog

urlpatterns=[
    path('',blog)
]