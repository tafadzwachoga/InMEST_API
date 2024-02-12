from django.contrib import admin
from main.models import Course
from .models import *

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'course_code', 'course_fee', 'course_status', 'course_date_created')
    list_filter = ('course_status', 'course_date_created')
    search_fields = ('course_name', 'course_code')

admin.site.register(Course, CourseAdmin)




