from rest_framework import serializers
from .models import Student, StudentCourse, Course

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course

class StudentCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentCourse
