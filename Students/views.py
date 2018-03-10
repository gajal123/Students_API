from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, render_to_response
from django.http import Http404, HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

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
#         messages.error(request, 'Logging In')
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
#         user = User.objects.filter(username=username, password=password)
#         messages.error(request, 'got pw')

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
        context = {
               'students' : students,
    }
        return render(request, 'home.html', context)
    return redirect('login')
