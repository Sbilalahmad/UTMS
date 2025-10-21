from .models import Schedule
from django.db.models import Q
def check_conflict(sched: Schedule, exclude_id=None):
    """
    Returns dict with keys 'room' and/or 'faculty' if conflict exists.
    """
    conflicts = {}
    qs = Schedule.objects.filter(semester=sched.semester, timeslot=sched.timeslot)
    if exclude_id:
        qs = qs.exclude(pk=exclude_id)
    if qs.filter(room=sched.room).exists():
        conflicts['room'] = 'Room already booked for this slot'
    if qs.filter(faculty=sched.faculty).exists():
        conflicts['faculty'] = 'Faculty already booked for this slot'
    return conflicts
