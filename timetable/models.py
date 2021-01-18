from django.db import models

# Create your models here.
class Route(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class Town(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class Stop(models.Model):
    name = models.CharField(max_length=200, null=True)
    town = models.ForeignKey(Town, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class Route_details(models.Model):
    route_id = models.ForeignKey(Route, on_delete=models.SET_NULL, null=True)
    stop_nr = models.IntegerField(null=False)
    stop_id = models.ForeignKey(Stop, on_delete=models.SET_NULL, null=True)
    time_diff = models.IntegerField(null=True)

    class Meta:
        unique_together = (("route_id", "stop_nr"),)

class Schedule(models.Model):
    route_id = models.ForeignKey(Route, on_delete=models.SET_NULL, null=True)
    start_time = models.TimeField(null=True)