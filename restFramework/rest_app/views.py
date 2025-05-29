from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from .models import person,student
from .serializers import personSerilizers,studentSerilizer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView

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


# Class-based view to handle GET and POST requests for all students
class studentView(APIView):
    # Handle GET request - Return a list of all students
    def get(self, request):
        students = student.objects.all()  # Fetch all student records
        serializer = studentSerilizer(students, many=True)  # Serialize list of students
        return Response(serializer.data)  # Return serialized data

    # Handle POST request - Create a new student
    def post(self, request):
        serializer = studentSerilizer(data=request.data)  # Deserialize incoming data
        if serializer.is_valid():  # Validate the data
            serializer.save()  # Save new student to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return errors if invalid

# Class-based view to handle GET, PUT, and DELETE requests for a single student using primary key
class studentDetailView(APIView):
    # Helper method to fetch student object or raise 404 if not found
    def get_object(self, pk):
        try:
            return student.objects.get(pk=pk)  # Try to fetch student by primary key
        except student.DoesNotExist:
            raise Http404  # Raise 404 error if not found

    # Handle GET request - Return details of a single student
    def get(self, request, pk):
        students = self.get_object(pk)  # Fetch student instance
        serializer = studentSerilizer(students)  # Serialize student data
        return Response(serializer.data)  # Return serialized data

    # Handle PUT request - Update student details
    def put(self, request, pk):
        students = self.get_object(pk)  # Fetch student instance
        serializer = studentSerilizer(students, data=request.data)  # Deserialize new data
        if serializer.is_valid():  # Validate the data
            serializer.save()  # Save updated student data
            return Response(serializer.data)  # Return updated data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return errors if invalid

    # Handle DELETE request - Delete the student
    def delete(self, request, pk):
        students = self.get_object(pk)  # Fetch student instance
        students.delete()  # Delete the student from database
        return Response(status=status.HTTP_204_NO_CONTENT)  # 204 = No Content (successfully deleted)
