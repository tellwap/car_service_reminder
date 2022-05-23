from django.contrib import admin
from .models import Car,CarInsuarance, CarMonitoring

# Register your models here.
admin.site.register(Car)
admin.site.register(CarInsuarance)
admin.site.register(CarMonitoring)

