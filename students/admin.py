from django.contrib import admin
from .models import Student, Course, StudentCourse

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(StudentCourse)
