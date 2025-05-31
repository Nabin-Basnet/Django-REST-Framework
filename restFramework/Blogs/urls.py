from django.urls import path,include
from .views import BlogViewSet,home,coommentsView
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'blogs',BlogViewSet,basename='blog')
router.register('comments',coommentsView,basename='comment')

urlpatterns=[
    path('',home),
    path('',include(router.urls)),
]