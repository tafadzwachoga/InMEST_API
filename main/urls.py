from django.urls import path
from . views import *

urlpatterns = [
    path("say_hello/", say_hello),
    path("filter_queries/<int:id>", filter_queries),
]