from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import person, student, teacher
from .serializers import personSerilizers, studentSerilizer, teacherSerilizer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics, mixins

# Basic view to confirm if the project is working
def home(request):
    return HttpResponse("Hello! here we are learning django rest_framework.")

# Function-based view to handle GET (list all persons) and POST (create person)
@api_view(['GET', 'POST'])
def personView(request):
    if request.method == 'GET':
        # Fetch all person records
        Person = person.objects.all()
        # Serialize the queryset
        serializer = personSerilizers(Person, many=True)
        # Return the serialized data
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        # Deserialize the incoming request data
        serializer = personSerilizers(data=request.data)
        if serializer.is_valid():
            # Save the data to the database if valid
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Return error if data is invalid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Function-based view to handle GET, PUT, DELETE operations for a single person
@api_view(['GET', 'PUT', 'DELETE'])
def personDetailView(request, pk):
    try:
        # Attempt to fetch person by primary key
        persons = person.objects.get(pk=pk)
    except:
        # Return 400 error if person is not found
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        # Serialize the person instance
        serializer = personSerilizers(persons)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        # Deserialize and update the person instance
        serializer = personSerilizers(persons, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # Delete the person record
        persons.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Class-based view for handling GET and POST operations for student model
class studentView(APIView):
    def get(self, request):
        # Fetch all student records
        students = student.objects.all()
        # Serialize the queryset
        serializer = studentSerilizer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Deserialize incoming data
        serializer = studentSerilizer(data=request.data)
        if serializer.is_valid():
            # Save if valid
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Class-based view for handling GET, PUT, DELETE for a single student
class studentDetailView(APIView):
    # Helper method to fetch student or raise 404
    def get_object(self, pk):
        try:
            return student.objects.get(pk=pk)
        except student.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        # Fetch and serialize student
        students = self.get_object(pk)
        serializer = studentSerilizer(students)
        return Response(serializer.data)

    def put(self, request, pk):
        # Fetch student and deserialize update data
        students = self.get_object(pk)
        serializer = studentSerilizer(students, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Delete the student instance
        students = self.get_object(pk)
        students.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Generic class-based view using mixins to handle GET (list) and POST (create) for teachers
class teachers(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = teacher.objects.all()  # Set queryset to all teacher records
    serializer_class = teacherSerilizer  # Define serializer class

    def get(self, request):
        # Return list of all teachers
        return self.list(request)

    def post(self, request):
        # Create new teacher record
        return self.create(request)

# Generic class-based view using mixins to handle GET (retrieve), PUT (update), and DELETE for a single teacher
class teacherDetailView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = teacher.objects.all()  # Set queryset to all teachers
    serializer_class = teacherSerilizer  # Define serializer class

    def get(self, request, pk):
        # Return a single teacher object
        return self.retrieve(request, pk)

    def put(self, request, pk):
        # Update a teacher object
        return self.update(request, pk)

    def delete(self, request, pk):
        # Delete a teacher object
        return self.destroy(request, pk)
