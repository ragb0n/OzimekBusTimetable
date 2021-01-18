from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Town)
admin.site.register(Stop)
admin.site.register(Route)
admin.site.register(Route_details)
admin.site.register(Schedule)