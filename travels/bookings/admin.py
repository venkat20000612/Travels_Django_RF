from django.contrib import admin
from.models import Bus, Seat

# Register your models here.


class Busadmin(admin.ModelAdmin):
    list_display = ('bus_name', 'bus_number', 'origin', 'destination')

admin.site.register(Bus, Busadmin)
admin.site.register(Seat)
