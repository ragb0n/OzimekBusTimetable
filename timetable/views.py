from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

from .models import *


def home(request):
    return render(request, 'timetable/home.html')


def routes(request):
    routes = Route.objects.all().order_by('name')

    return render(request, 'timetable/timetables.html', {'routes': routes})


def route(request, pk):
    routes = Route.objects.all().order_by('name')
    selected_route_name = Route.objects.get(pk=pk)
    details = Route_details.objects.filter(route_id=pk)
    time_diffs = details.values_list("time_diff", flat=True)
    starting_hours = Schedule.objects.values_list('start_time', flat=True).filter(route_id=pk)

    time_list = []
    for hour in starting_hours:
        last_stop_time = hour
        time_list_2 = []
        for diff in time_diffs:
            if last_stop_time.minute + diff > 59:
                minutes_to_full_hour = diff - (59 - last_stop_time.minute)
                last_stop_time = datetime.time(last_stop_time.hour + 1, last_stop_time.minute - last_stop_time.minute
                                               + minutes_to_full_hour - 1)
            else:
                last_stop_time = datetime.time(last_stop_time.hour + 0, last_stop_time.minute + diff)
            time_list_2.append(last_stop_time)
        time_list.append(time_list_2)

    context = {'routes': routes, 'details': details, 'time_list': time_list, 'starting_hours': starting_hours,
               'selected_route_name': selected_route_name}
    return render(request, 'timetable/timetable.html', context)
