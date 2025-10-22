from .models import Schedule

def check_conflict(sched: Schedule, exclude_id=None):
    """
    Return dict with keys 'room' / 'faculty' if clash exists.
    exclude_id = pk of record being edited (so we don’t clash with itself).
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