from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import *

def home(request):
    routes = Route.objects.all()
    details = Route_details.objects.filter(route_id=1)
    hours = Schedule.objects.filter(route_id = 1)
    context = {'routes': routes, 'details': details, 'hours': hours}

    return render(request, 'timetable/dashboard.html', context)
