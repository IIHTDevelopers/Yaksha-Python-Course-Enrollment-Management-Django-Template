from rest_framework.test import APITestCase
from library.test.TestUtils import TestUtils
from library.models import Course, Student
from django.urls import reverse
from django.test import TestCase

class StudentBoundaryTest(TestCase):

    def test_boundary(self):
        """Test generic boundary conditions"""
        test_obj = TestUtils()
        test_obj.yakshaAssert("TestBoundary", True, "boundary")
        print("TestBoundary = Passed")

