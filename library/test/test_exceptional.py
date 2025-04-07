
from rest_framework.test import APITestCase
from django.db import IntegrityError
from library.test.TestUtils import TestUtils
from django.urls import reverse
from unittest.mock import patch
from django.urls import get_resolver
from django.test import TestCase
from library.models import Course, Student
from library.admin import CourseAdmin, StudentAdmin
from library.admin import StudentInline
from django.core.exceptions import ValidationError


class StudentExceptionalTest(TestCase):

    def test_duplicate_email(self):
        """Test if creating a student with duplicate email raises an error"""
        test_obj = TestUtils()
        try:
            course = Course.objects.create(name="Data Science", description="Learn Data Science", start_date="2025-06-01")
            Student.objects.create(first_name="Alice", last_name="Smith", email="alice@example.com", course=course)
            duplicate_student = Student(first_name="Bob", last_name="Smith", email="alice@example.com", course=course)
            
            try:
                duplicate_student.save()
                test_obj.yakshaAssert("TestDuplicateEmail", False, "exceptional")
                print("TestDuplicateEmail = Failed")
            except:
                test_obj.yakshaAssert("TestDuplicateEmail", True, "exceptional")
                print("TestDuplicateEmail = Passed")
        except:
            test_obj.yakshaAssert("TestDuplicateEmail", False, "exceptional")
            print("TestDuplicateEmail = Failed")

    def test_course_deletion_cascade(self):
        """Test if deleting a course also deletes related students"""
        test_obj = TestUtils()
        try:
            course = Course.objects.create(name="Web Development", description="Learn Web Dev", start_date="2025-07-01")
            student = Student.objects.create(first_name="Eve", last_name="Taylor", email="eve@example.com", course=course)
            
            course.delete()
            student_exists = Student.objects.filter(email="eve@example.com").exists()
            
            if not student_exists:
                test_obj.yakshaAssert("TestCourseDeletionCascade", True, "exceptional")
                print("TestCourseDeletionCascade = Passed")
            else:
                test_obj.yakshaAssert("TestCourseDeletionCascade", False, "exceptional")
                print("TestCourseDeletionCascade = Failed")
        except:
            test_obj.yakshaAssert("TestCourseDeletionCascade", False, "exceptional")
            print("TestCourseDeletionCascade = Failed")
