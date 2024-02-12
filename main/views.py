from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View
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