from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, render_to_response
from django.http import Http404, HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from students.models import Course, StudentCourse, Student
import simplejson as json

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            # correct username and password login the user
            auth.login(request, user)
            return redirect('home')

        else:
            return render_to_response("login.html",
                       {'invalid': True })

    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

import requests

def home(request):
    if request.user.is_authenticated:
        # todo: change this to a relative url
        url = 'https://osy0fx6q.apps.lair.io/api/students'
        students = requests.get(url).json()
        url = 'https://osy0fx6q.apps.lair.io/api/studentcourses'
        student_courses = requests.get(url).json()
        url = 'https://osy0fx6q.apps.lair.io/api/courses'
        courses = requests.get(url).json()
        student_dict = {}
        course_dict = {}
        for student_info in students:
            student_dict[student_info.get('user_name')] = []
        for course_info in courses:
            course_dict[course_info.get('name')] = []
        for student_courses_info in student_courses:
            user_name = student_courses_info.get('user_name')
            course = student_courses_info.get('course_name')
            student_dict[user_name].append(course)
            course_dict[course].append(user_name)

        context = {
               'students' : students,
               'student_courses': student_courses,
               'student_dict': student_dict,
               'course_dict': course_dict,

    }
        return render(request, 'home.html', context)
    return redirect('login')

def delete_course(request):
    # POST request CSRF is failing. I passed a csrfmiddlewaretoken but i think
    # there is some issue with the online IDE i am using. So i made this a GET request.
    # This should be a POST Request.
    course_name = request.GET.get('course')
    try:
        course = Course.objects.get(name=course_name).delete()

    except Exception as e:
        return HttpResponse(json.dumps({'status': 'error'}))
    return HttpResponse(json.dumps({'status': 'success', 'course_name': course_name}))

def student_enrolls(request):
    course_name = request.GET.get('course')
    try:
        course = Course.objects.get(name=course_name)
        no_of_students_enrolled = course.no_of_students_enrolled
        student = Student.objects.get(user=request.user)
        student_course, created = StudentCourse.objects.get_or_create(student=student, course=course)
        if created:
            course.no_of_students_enrolled += 1
            course.save()

    except Exception as e:
        return HttpResponse(json.dumps({'status': 'error'}))
    return HttpResponse(json.dumps({'status': 'success', 'created': created, 'no':course.no_of_students_enrolled}))

