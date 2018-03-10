
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.views.generic.base import TemplateView
from Students import views

urlpatterns = [
    url(r'^home/$', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logout.html'}, name='logout'),
    url(r'^register/', views.register, name='register'),
    path('api/', include('students.urls', namespace='students')),
]
# urlpatterns += [
#     path('accounts/', include('django.contrib.auth.urls')),
# ]
