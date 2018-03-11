from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Course(models.Model):
    name = models.CharField(max_length=50)
    no_of_students_enrolled = models.IntegerField(max_length=None, blank=True, default=0)

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Cources"

    def __str__(self):
        return '{} - {} Students'.format(self.name, self.no_of_students_enrolled)


class Student(models.Model):
    user = models.ForeignKey(User , null = True, on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=50, null=True)
#     last_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)
post_save.connect(create_or_update_user_profile, sender=User)


class StudentCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.student.user.username, self.course.name)
