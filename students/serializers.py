from rest_framework import serializers
from .models import Student, StudentCourse, Course

class StudentSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Student
        fields = ('id', 'user', 'user_name')

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ('id', 'name', 'no_of_students_enrolled')

class StudentCourseSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='student.user.username', read_only=True)
    course_name = serializers.CharField(source='course.name', read_only=True)
    class Meta:
        model = StudentCourse
        fields = ('id', 'student', 'course', 'user_name', 'course_name')
