from django.shortcuts import render
from .models import Blog,Comment
from django.http import HttpResponse
from rest_framework import viewsets
from .serializer import blogSerializer,commentsSerializer
from rest_framework.filters import SearchFilter,OrderingFilter

# Create your views here.
def home(request):
    return HttpResponse("this is blog")

class BlogViewSet(viewsets.ModelViewSet):  # Renamed class
    queryset = Blog.objects.all()
    serializer_class = blogSerializer
    lookup_field='pk'
    filter_backends=[SearchFilter,OrderingFilter]  # search filter are for searching & orderingfilter for order the data by id either bt asc or dec
    search_fields=['blog_title','blog_body']
    ordering_fields=['id']


class coommentsView(viewsets.ModelViewSet):
    queryset=Comment.objects.all()
    serializer_class=commentsSerializer
    lookup_field='pk'