from django.urls import path
from .views import home,personView,personDetailView,studentView,studentDetailView,teachers,teacherDetailView,employee,employeeDetailView


urlpatterns=[
    path('',home),
    path('persons',personView),
    path('person/<int:pk>/',personDetailView),

    path('student',studentView.as_view()),
    path('student/<int:pk>/',studentDetailView.as_view()),

    path('teachers',teachers.as_view()),
    path('teachers/<int:pk>',teacherDetailView.as_view()),

    path('employee',employee.as_view()),
    path('employee/<int:pk>',employeeDetailView.as_view()),
]