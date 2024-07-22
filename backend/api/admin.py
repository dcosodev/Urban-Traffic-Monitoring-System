from django.contrib import admin
from .models import TrafficFlow, TrafficIncident, TrafficSensor

admin.site.register(TrafficFlow)
admin.site.register(TrafficIncident)
admin.site.register(TrafficSensor)
