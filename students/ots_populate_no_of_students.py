from students.models import Student, Course, StudentCourse
from Accounts.views import *

def ots_populate_no_of_students():
    url = 'https://osy0fx6q.apps.lair.io/api/students'
    students = requests.get(url).json()
    url = 'https://osy0fx6q.apps.lair.io/api/studentcourses'
    student_courses = requests.get(url).json()
    url = 'https://osy0fx6q.apps.lair.io/api/courses'
    courses = requests.get(url).json()
    student_dict = {}
    course_dict = {}
    for course_info in courses:
        course_dict[course_info.get('name')] = []
    for student_courses_info in student_courses:
        user_name = student_courses_info.get('user_name')
        course = student_courses_info.get('course_name')
        course_dict[course].append(user_name)
    print(course_dict)
    courses = Course.objects.all()
    for course in courses:
        students_list = course_dict.get(course.name)
        course.no_of_students_enrolled = len(students_list)
        course.save()


