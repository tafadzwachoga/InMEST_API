from django.urls import path
from . views import *

urlpatterns = [
    path("say_hello/", say_hello),
    path("filter_queries/<int:id>", filter_queries),
    path("filter_queries/", filter_queries),
    path("queries/", QueryView.as_view(), name="queries"),
    path("schedules/fetch/", fetch_class_schedules),
    path("schedules/create/", create_class_schedule),
]