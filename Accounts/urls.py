
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
    url(r'^leave_course', views.leave_course, name='leave_course'),
    url(r'^remove_student_from_course', views.remove_student_from_course, name='remove_student_from_course'),
    url(r'^enroll_student_in_course', views.enroll_student_in_course, name='enroll_student_in_course'),
    url(r'^add_course', views.add_course, name='add_course'),
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
