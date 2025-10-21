from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Department(models.Model):
    name = models.CharField(max_length=120)
    code = models.CharField(max_length=10, unique=True)
    def __str__(self):
        return f"{self.code} - {self.name}"

class Course(models.Model):
    name = models.CharField(max_length=120)
    code = models.CharField(max_length=20, unique=True)
    credits = models.PositiveSmallIntegerField(default=3)   
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    def __str__(self):
        return self.code
    
class Faculty(models.Model):
    user = models.OneToOneField('accounts.User', on_delete=models.CASCADE, limit_choices_to={'role': 'faculty'})
    name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    availability = models.JSONField(default=dict, blank=True)  # e.g. {"mon": ["08:00", "17:00"]}
    def __str__(self):
        return self.name

class Room(models.Model):
    ROOM_TYPES = (
        ('lecture', 'Lecture Hall'),
        ('lab', 'Lab'),
        ('tutorial', 'Tutorial Room'),
    )
    name = models.CharField(max_length=50, unique=True)
    capacity = models.PositiveIntegerField()
    type = models.CharField(max_length=10, choices=ROOM_TYPES)
    def __str__(self):
        return self.name

class Timeslot(models.Model):
    DAYS = [(i, i) for i in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']]
    day_of_week = models.CharField(max_length=10, choices=DAYS)
    start_time = models.TimeField()
    end_time = models.TimeField()

class Meta:
    unique_together = ('day_of_week', 'start_time', 'end_time')

def __str__(self):
    return f"{self.day_of_week} {self.start_time}–{self.end_time}"