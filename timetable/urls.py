from django.urls import path
from . import views
from timetable.views import *

urlpatterns = [
    path('', views.home, name="home"),
    path('routes', views.routes, name="timetables"),
    path('routes/<str:pk>/', views.route, name="timetable"),
]
