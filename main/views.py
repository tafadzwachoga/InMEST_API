from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.models import*
from main.serializers import*
# Create your views here.

def json(request):
    return JsonResponse(request, 'main/json.html')

def http_response(request):
    return HttpResponse(request, 'main/index.html')

def say_hello(request):
    return HttpResponse("<h1>Hello, World!</h1>")


def filter_queries(request, id):
    return JsonResponse({
        "id": id,
        "title": "Filter Queries",
        "description": "This is a description of the filter queries",
        "status": "completed",
        "submited_by": "Tafadzwa Choga"
    })

class QueryView(View):
    pass

@api_view(['GET'])
def fetch_class_schedules(request):
    #1. Retrieve from db all class schedules
  queryset = ClassSchedule.objects.all()

    #2. Return queryset result as response/Serialize the data?
  
  serializer = ClassScheduleSerializer(queryset, many=True)
  return Response({"data":serializer.data}, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_class_schedule(request):
    title = request.data.get('title')
    description = request.data.get('description')
    start_time = request.data.get('start_time')
    end_time = request.data.get('end_time')
    day = request.data.get('day')
    cohort_id = request.data.get('cohort_id')
    course_id = request.data.get('course_id')
    facilitator_id = request.data.get('facilitator_id')
    is_repeated = request.data.get('is_repeated')
    repeat_frequency = request.data.get('repeat_frequency')
    meeting_type = request.data.get('meeting_type')

    if not title:
        return Response({"error": "Title is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    cohort = None
    facilitator = None
    course = None


    try:
        cohort = Cohort.objects.get(id=cohort_id)
    except Cohort.DoesNotExist:
        return Response({"error": "Cohort not found"}, status=status.HTTP_404_NOT_FOUND)
    
    try:
        course = Course.objects.get(id=cohort_id)
    except Course.DoesNotExist:
        return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)
    
    try:
        facilitator = IMUser.objects.get(id=cohort_id)
    except IMUser.DoesNotExist:
        return Response({"error": "IMUser not found"}, status=status.HTTP_404_NOT_FOUND)
    
    class_schedule = ClassSchedule.objects.create(
        title=title,
        description=description,
        start_time=start_time,
        end_time=end_time,
        day=day,
        cohort=cohort,
        course=course,
        facilitator=facilitator,
        is_repeated=is_repeated,
        repeat_frequency=repeat_frequency,
        meeting_type=meeting_type
    )

    class_schedule.save()

    serializer = ClassScheduleSerializer(class_schedule)
    return Response({"message": "Schedule successfully created","data": serializer.data}, status=status.HTTP_201_CREATED)
    
