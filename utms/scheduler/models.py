from django.db import models
from core.models import Course, Faculty, Room, Timeslot

class Schedule(models.Model):
    SEMESTER_CHOICES = (('Fall', 'Fall'), ('Spring', 'Spring'), ('Summer', 'Summer'))
    course    = models.ForeignKey(Course, on_delete=models.CASCADE)
    faculty   = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    room      = models.ForeignKey(Room, on_delete=models.CASCADE)
    timeslot  = models.ForeignKey(Timeslot, on_delete=models.CASCADE)
    semester  = models.CharField(max_length=10, choices=SEMESTER_CHOICES)

    class Meta:
        unique_together = ('course', 'semester')

    def __str__(self):
        return f"{self.course.code} | {self.faculty.name} | {self.room} | {self.timeslot}"