from .models import Schedule
from core.models import Course, Faculty, Room, Timeslot
import random

def run_scheduler(semester: str):
    """
    Greedy timetable generator.  Returns list of UNSAVED Schedule objects.
    Avoids double-booking faculty or rooms in the same timeslot.
    """
    courses   = list(Course.objects.all())
    faculty   = list(Faculty.objects.filter(user__role='faculty'))
    rooms     = list(Room.objects.all())
    timeslots = list(Timeslot.objects.all())

    existing         = Schedule.objects.filter(semester=semester)
    booked_rooms     = {(e.room_id, e.timeslot_id) for e in existing}
    booked_faculty   = {(e.faculty_id, e.timeslot_id) for e in existing}

    output = []
    for course in courses:
        if existing.filter(course=course).exists():
            continue
        random.shuffle(faculty); random.shuffle(rooms); random.shuffle(timeslots)
        assigned = False
        for fac in faculty:
            if fac.department != course.department:  # simple dept match
                continue
            for room in rooms:
                for ts in timeslots:
                    if (room.id, ts.id) in booked_rooms or (fac.id, ts.id) in booked_faculty:
                        continue
                    output.append(Schedule(
                        course=course, faculty=fac, room=room, timeslot=ts, semester=semester))
                    booked_rooms.add((room.id, ts.id))
                    booked_faculty.add((fac.id, ts.id))
                    assigned = True
                    break
                if assigned: break
            if assigned: break
        if not assigned:
            print(f"[WARN] Could not schedule {course.code}")
    return output