from django.urls import path
from django.conf.urls import url
from rest_framework import routers
from students.views import StudentViewSet, CourseViewSet, StudentCourseViewSet

# urlpatterns = [
#     path('', views.index, name='index'),
# ]
app_name = 'students'

router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'studentcourses', StudentCourseViewSet)

urlpatterns = router.urls
