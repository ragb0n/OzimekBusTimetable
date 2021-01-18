from django.urls import path
from . import views
from timetable.views import *

urlpatterns = [
    path('', views.home),
]
