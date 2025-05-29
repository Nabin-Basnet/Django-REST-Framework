from django.urls import path
from .views import home,personView,personDetailView,studentView,studentDetailView


urlpatterns=[
    path('',home),
    path('persons',personView),
    path('student',studentView.as_view()),
    path('student/<int:pk>/',studentDetailView.as_view()),
    path('person/<int:pk>/',personDetailView),
]