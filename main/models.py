from django.db import models
from django.db import models
from django.contrib.auth.models import User
from users.models import IMUser  

class Course(models.Model):

    course_name=models.CharField(max_length=1000)
    course_description = models.TextField(default = "N/A", blank=True, null = True)
    course_date_created =models.DateTimeField(auto_now_add=True, blank = True, null = True)
    course_date_modified =models.DateTimeField(auto_now =True, blank = True, null = True)

    def __str__(self):
        return self.course_name

# Assuming you have a Cohort model defined somewhere
class Cohort(models.Model):
    # Your fields for Cohort model
    pass



class ClassSchedule(models.Model):

    REPEAT_FREQUENCY = (
        ('Daily', 'Daily'),
        ('Weekly', 'Weekly'),
        ('Monthly', 'Monthly'),
    )


    MEETING_TYPES = (
        ('Lecture', 'Lecture'),
        ('Workshop', 'Workshop'),
        ('Seminar', 'Seminar'),
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date_and_time = models.DateTimeField()
    end_date_and_time = models.DateTimeField()
    is_repeated = models.BooleanField(default=False)
    repeat_frequency = models.IntegerField(null=True, blank=True)  # Adjust according to your requirements
    is_active = models.BooleanField(default=True)
    organizer = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='organized_classes')
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE, related_name='class_schedules')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, related_name='class_course')
    facilitator = models.ForeignKey(IMUser, on_delete=models.CASCADE, null=True, related_name='facilitated_classes')
    venue = models.CharField(max_length=255)


class ClassAttendance(models.Model):

    class_schedule = models.ForeignKey(ClassSchedule, on_delete=models.CASCADE, related_name='attendances')
    attendee = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='attended_classes')
    is_present = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='created_attendances')

class QueryStatusChoices(models.TextChoices):
    PENDING = 'PE', 'Pending'
    IN_PROGRESS = 'IP', 'In Progress'
    DECLINED = 'DL', 'Declined'
    RESOLVED = 'RE', 'Resolved'

class Query(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()
    submitted_by = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='submitted_queries')
    assigned_to = models.ForeignKey(IMUser, on_delete=models.CASCADE, null=True, related_name='assigned_queries')
    resolution_status = models.CharField(max_length=2, choices=QueryStatusChoices.choices, default=QueryStatusChoices.PENDING)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='authored_queries')

    def __str__(self):
        return self.title

class QueryComment(models.Model):

    query = models.ForeignKey(Query, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='commented_queries')
