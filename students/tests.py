from django.test import TestCase
from .models import Student

class ModelTestCase(TestCase):

    def setUp(self):
        self.student_name = "Gajal"
        self.student = Student(name=self.student_name)

    def test_model_can_create_a_student(self):
        old_count = Student.objects.count()
        self.student.save()
        new_count = Student.objects.count()
        self.assertNotEqual(old_count, new_count)
