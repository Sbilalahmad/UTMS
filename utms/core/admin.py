from django.contrib import admin
from .models import Department, Course, Faculty, Room, Timeslot

admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Faculty)
admin.site.register(Room)
admin.site.register(Timeslot)