from django.urls import path
from .views import home,personView,personDetailView


urlpatterns=[
    path('',home),
    path('persons',personView),
    path('person/<int:pk>/',personDetailView),
]