from django.urls import path,include
from .views import home,personView,personDetailView,studentView,studentDetailView,teachers,teacherDetailView,EmployeeListCreateView,EmployeeDetailView,staffsView,addressView
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('staff',staffsView,basename='staff')
router.register(r'address',addressView,basename='address')

urlpatterns=[
    path('',home),
    path('persons',personView),
    path('person/<int:pk>/',personDetailView),

    path('student',studentView.as_view()),
    path('student/<int:pk>/',studentDetailView.as_view()),

    path('teachers',teachers.as_view()),
    path('teachers/<int:pk>',teacherDetailView.as_view()),

    path('employee',EmployeeListCreateView.as_view()),
    path('employee/<int:pk>',EmployeeDetailView.as_view()),

    path('',include(router.urls))
]