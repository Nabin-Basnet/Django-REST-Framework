from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import person, student, teacher, Employee,staff,address
from .serializers import personSerilizers, studentSerilizer, teacherSerilizer, EmployeeSerilizer,staffSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics, mixins,viewsets

# Basic view to verify that the project is running
def home(request):
    return HttpResponse("Hello! Here we are learning Django REST Framework.")

# Function-based view to list all persons or create a new person
@api_view(['GET', 'POST'])
def personView(request):
    if request.method == 'GET':
        # Retrieve all person records from the database
        Person = person.objects.all()
        # Serialize and return the list of persons
        serializer = personSerilizers(Person, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        # Deserialize the input data to create a new person
        serializer = personSerilizers(data=request.data)
        if serializer.is_valid():
            # Save the new person to the database
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Return validation errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Function-based view to retrieve, update, or delete a specific person by ID
@api_view(['GET', 'PUT', 'DELETE'])
def personDetailView(request, pk):
    try:
        # Try to retrieve the person by primary key
        persons = person.objects.get(pk=pk)
    except:
        # Return error if the person is not found
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        # Serialize and return the person data
        serializer = personSerilizers(persons)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        # Deserialize input and update the person record
        serializer = personSerilizers(persons, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        # Return validation errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # Delete the specified person record
        persons.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Class-based view to list all students or create a new student
class studentView(APIView):
    def get(self, request):
        # Retrieve all student records
        students = student.objects.all()
        # Serialize and return the list
        serializer = studentSerilizer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Deserialize and create a new student
        serializer = studentSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Return validation errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Class-based view to retrieve, update, or delete a specific student
class studentDetailView(APIView):
    def get_object(self, pk):
        # Helper function to get a student by ID or raise 404
        try:
            return student.objects.get(pk=pk)
        except student.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        # Retrieve and return student data
        students = self.get_object(pk)
        serializer = studentSerilizer(students)
        return Response(serializer.data)

    def put(self, request, pk):
        # Update a student record with input data
        students = self.get_object(pk)
        serializer = studentSerilizer(students, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        # Return validation errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Delete a student record
        students = self.get_object(pk)
        students.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Generic view using mixins to list or create teacher records
class teachers(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = teacher.objects.all()
    serializer_class = teacherSerilizer

    def get(self, request):
        # Return list of all teachers
        return self.list(request)

    def post(self, request):
        # Create a new teacher record
        return self.create(request)

# Generic view using mixins to retrieve, update, or delete a specific teacher
class teacherDetailView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = teacher.objects.all()
    serializer_class = teacherSerilizer

    def get(self, request, pk):
        # Retrieve and return a single teacher
        return self.retrieve(request, pk)

    def put(self, request, pk):
        # Update an existing teacher record
        return self.update(request, pk)

    def delete(self, request, pk):
        # Delete a teacher record
        return self.destroy(request, pk)

##Generic class-based view to handle listing all employees and creating a new employee
class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()  # Fetch all employee records from the database
    serializer_class = EmployeeSerilizer  # Use the Employee serializer to handle input/output

# Generic class-based view to retrieve, update, or delete a specific employee by primary key (pk)
class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()  # Use all employee records as the source queryset
    serializer_class = EmployeeSerilizer  # Use the same serializer as above
    lookup_field = 'pk'  # Identify records using the 'pk' (primary key) field


# Custom ViewSet for handling staff-related CRUD operations
class staffsView(viewsets.ViewSet):

    # Handle GET request to list all staff records
    def list(self, request):
        queryset = staff.objects.all()
        serializer = staffSerializer(queryset, many=True)
        return Response(serializer.data)

    # Handle POST request to create a new staff record
    def create(self, request):
        serializer = staffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    # Handle GET request to retrieve a specific staff record by ID
    def retrieve(self, request, pk):
        staffs = get_object_or_404(staff, pk=pk)
        serializer = staffSerializer(staffs)
        return Response(serializer.data)

    # Handle PUT request to update a specific staff record by ID
    def update(self, request, pk):
        staffs = get_object_or_404(staff, pk=pk)
        serializer = staffSerializer(staffs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    # Handle DELETE request to remove a specific staff record by ID
    def delete(self, request, pk):
        staffs = get_object_or_404(staff, pk=pk)
        staffs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
