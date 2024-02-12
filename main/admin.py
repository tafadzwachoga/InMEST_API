from django.contrib import admin
from .models import *
from django.contrib import admin
from .models import ClassSchedule, ClassAttendance, Query, QueryComment

# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    list_display = ("course_name", "course_description", "course_date_created", "course_date_modified")


class ClassScheduleAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'start_date_and_time', 'end_date_and_time', 'is_repeated', 'repeat_frequency', 'is_active', 'organizer', 'cohort', 'venue')
    # Add other configurations as needed

class ClassAttendanceAdmin(admin.ModelAdmin):
    list_display = ('class_schedule', 'attendee', 'is_present', 'date_created', 'date_modified', 'author')
    # Add other configurations as needed

class QueryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'submitted_by', 'assigned_to', 'resolution_status', 'date_created', 'date_modified', 'author')
    # Add other configurations as needed

class QueryCommentAdmin(admin.ModelAdmin):
    list_display = ('query', 'comment', 'date_created', 'date_modified', 'author')
    # Add other configurations as needed

admin.site.register(Course, CourseAdmin) 
