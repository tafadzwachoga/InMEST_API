from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

# Create your views here.

def user_profile(request):
    return JsonResponse({
        "name": "Tafadzwa Choga",
        "age": 30,
        "city": "New York"
    })
