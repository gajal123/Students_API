from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, StudentCourse, Course
from rest_framework import viewsets
from .serializers import StudentSerializer, CourseSerializer, StudentCourseSerializer

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class StudentCourseViewSet(viewsets.ModelViewSet):
    queryset = StudentCourse.objects.all()
    serialiser_class = StudentCourseSerializer
