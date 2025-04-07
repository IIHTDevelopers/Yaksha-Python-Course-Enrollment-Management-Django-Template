from django.contrib import admin
from .models import Course, Student

class StudentInline(admin.TabularInline):
    pass

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass

