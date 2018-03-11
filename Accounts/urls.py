
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.views.generic.base import TemplateView
from Accounts import views

urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^delete_course', views.delete_course, name='delete_course'),
    url(r'^delete_student', views.delete_student, name='delete_student'),
    url(r'^student_enrolls', views.student_enrolls, name='student_enrolls'),
    path('admin/', admin.site.urls),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^register/', views.register, name='register'),
    path('api/', include('students.urls', namespace='students')),
]
# urlpatterns += [
#     path('accounts/', include('django.contrib.auth.urls')),
# ]
