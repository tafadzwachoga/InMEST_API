from django.db import models

# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=200)
    course_code = models.CharField(max_length=10)
    course_description = models.TextField()
    course_duration = models.IntegerField(blank=True, null=True)
    course_date_created = models.DateTimeField(blank=True, null=True)
    course_fee = models.IntegerField()
    course_status = models.BooleanField(default=True)

    def __str__(self):
        return self.course_name