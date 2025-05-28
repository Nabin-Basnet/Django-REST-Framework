from django.shortcuts import render
from django.http import HttpResponse
from .models import person
from .serializers import personSerilizers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Basic view to test if the project is running
def home(request):
    return HttpResponse("Hello! here we are learning django rest_framework.")

# View to handle GET and POST requests for listing all persons and creating a new person
@api_view(['GET', 'POST'])
def personView(request):
    # Handle GET request - Return a list of all persons
    if request.method == 'GET':
        Person = person.objects.all()  # Fetch all person records from the database
        serializer = personSerilizers(Person, many=True)  # Serialize all person data
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Handle POST request - Add a new person
    elif request.method == 'POST':
        serializer = personSerilizers(data=request.data)  # Deserialize incoming data
        if serializer.is_valid():  # Validate the data
            serializer.save()  # Save the new person to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # If data is invalid, return a 400 error with the data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View to handle GET, PUT, and DELETE requests for a single person using their primary key
@api_view(['GET', 'PUT', 'DELETE'])
def personDetailView(request, pk):
    try:
        # Try to fetch the person with the given primary key (pk)
        persons = person.objects.get(pk=pk)
    except:
        # If not found, return 400 Bad Request
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    # Handle GET request - Return details of a single person
    if request.method == 'GET':
        serializer = personSerilizers(persons)  # Serialize the person object
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Handle PUT request - Update details of the person
    elif request.method == 'PUT':
        serializer = personSerilizers(persons, data=request.data)  # Deserialize new data
        if serializer.is_valid():
            serializer.save()  # Save updated person info
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    # Handle DELETE request - Delete the person record
    elif request.method == 'DELETE':
        persons.delete()  # Delete the person from database
        return Response(status=status.HTTP_204_NO_CONTENT)  # 204 = No Content (successfully deleted)
