from django.shortcuts import render
from django.http import HttpResponse
from .models import person
from .serializers import personSerilizers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
def home(request):
    return HttpResponse("Hello! here we are learning django rest_frameeork.")

@api_view(['GET','POST'])
def personView(request):
    if request.method=='GET':
        Person=person.objects.all()
        serializer=personSerilizers(Person,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    elif request.method=="POST":
        serializer=personSerilizers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET','PUT','DELETE'])
def personDetailView(request,pk):
    try:
        persons=person.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method=="GET":
        serializer=personSerilizers(persons)
        return Response(serializer.data,status=status.HTTP_200_OK)

    elif request.method=="PUT":
        serializer=personSerilizers(persons,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method=="DELETE":
        persons.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)
    
# def
    
