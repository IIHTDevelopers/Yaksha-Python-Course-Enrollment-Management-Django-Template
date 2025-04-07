from django.urls import reverse
from rest_framework.test import APITestCase
from django.test import TestCase
from library.test.TestUtils import TestUtils
from django.contrib.admin.sites import site
from library.models import Course, Student
from library.admin import CourseAdmin, StudentAdmin
from library.admin import StudentInline

class StudentFunctionalTest(TestCase):
    
    def test_create_course(self):
        """Test if a course is created successfully"""
        test_obj = TestUtils()
        try:
            course = Course.objects.create(name="Django Basics", description="Learn Django", start_date="2025-04-01")
            if course:
                test_obj.yakshaAssert("TestCreateCourse", True, "functional")
                print("TestCreateCourse = Passed")
            else:
                test_obj.yakshaAssert("TestCreateCourse", False, "functional")
                print("TestCreateCourse = Failed")
        except:
            test_obj.yakshaAssert("TestCreateCourse", False, "functional")
            print("TestCreateCourse = Failed")

    def test_create_student(self):
        """Test if a student is created and linked to a course successfully"""
        test_obj = TestUtils()
        try:
            course = Course.objects.create(name="Python Programming", description="Learn Python", start_date="2025-05-01")
            student = Student.objects.create(first_name="John", last_name="Doe", email="john.doe@example.com", course=course)
            if student and student.course == course:
                test_obj.yakshaAssert("TestCreateStudent", True, "functional")
                print("TestCreateStudent = Passed")
            else:
                test_obj.yakshaAssert("TestCreateStudent", False, "functional")
                print("TestCreateStudent = Failed")
        except:
            test_obj.yakshaAssert("TestCreateStudent", False, "functional")
            print("TestCreateStudent = Failed")



    def test_admin_inline_registered(self):
        """Test if inline editing is enabled in the admin panel"""
        test_obj = TestUtils()
        
        try:
            if Course not in site._registry:
                test_obj.yakshaAssert("TestAdminInlineRegistered", False, "functional")
                print("TestAdminInlineRegistered = Failed")
                return
            
            admin_registered = isinstance(site._registry[Course], CourseAdmin)
            inline_registered = any(issubclass(i, StudentInline) for i in site._registry[Course].inlines)

            if admin_registered and inline_registered:
                test_obj.yakshaAssert("TestAdminInlineRegistered", True, "functional")
                print("TestAdminInlineRegistered = Passed")
            else:
                test_obj.yakshaAssert("TestAdminInlineRegistered", False, "functional")
                print("TestAdminInlineRegistered = Failed")

        except Exception as e:
            test_obj.yakshaAssert("TestAdminInlineRegistered", False, "functional")
            print("TestAdminInlineRegistered = Failed")