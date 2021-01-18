from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

from .models import *

def home(request):
    selected_route_id = 2
    routes = Route.objects.all()
    details = Route_details.objects.filter(route_id=selected_route_id)
    time_diffs = details.values_list("time_diff", flat=True)
    starting_hours = Schedule.objects.values_list('start_time', flat=True).filter(route_id = selected_route_id)

    time_list = []
    for hour in starting_hours:
        last_stop_time = hour
        time_list_2 = []
        for diff in time_diffs:
            if last_stop_time.minute + diff > 59:
                last_stop_time = datetime.time(last_stop_time.hour + 1, last_stop_time.minute - last_stop_time.minute + diff)
            else:
                last_stop_time = datetime.time(last_stop_time.hour + 0, last_stop_time.minute + diff)
            time_list_2.append(last_stop_time)
        time_list.append(time_list_2)

    context = {'routes': routes, 'details': details, 'time_list': time_list, 'starting_hours': starting_hours}
    return render(request, 'timetable/timetables.html', context)
