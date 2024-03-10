from rest_framework import serializers


class CourseSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    description = serializers.CharField()
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    is_active = serializers.BooleanField()
    author = serializers.IntegerField()
    
class UserSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    username = serializers.CharField()

class ClassScheduleSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    description = serializers.CharField()
    start_date_and_time = serializers.DateTimeField()
    end_date_and_time = serializers.DateTimeField()
    is_repeated = serializers.BooleanField()
    repeat_frequency = serializers.IntegerField()
    is_active = serializers.BooleanField()
    organizer = serializers.IntegerField()
    cohort = serializers.IntegerField()
    venue = serializers.CharField() 

class ClassAttendanceSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    class_schedule = serializers.IntegerField()
    attendee = serializers.IntegerField()
    is_present = serializers.BooleanField()
    date_created = serializers.DateTimeField()
    date_modified = serializers.DateTimeField()
    author = serializers.IntegerField()

class QuerySerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    description = serializers.CharField()
    submitted_by = serializers.IntegerField()
    assigned_to = serializers.IntegerField()
    resolution_status = serializers.CharField()
    date_created = serializers.DateTimeField()
    date_modified = serializers.DateTimeField()
    author = serializers.IntegerField()     