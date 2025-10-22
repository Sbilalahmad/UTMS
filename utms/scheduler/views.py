from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Schedule
from .algorithm import run_scheduler
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Schedule
from .utils import check_conflict
from core.models import Room, Timeslot, Faculty

def admin_check(u): return u.is_authenticated and u.role == 'admin'

@login_required
@user_passes_test(admin_check)
def generate_timetable(request):
    if request.method == 'POST':
        sem = request.POST.get('semester')
        if not sem:
            messages.error(request, "Semester required")
            return redirect('scheduler:generate')
        created = run_scheduler(sem)
        Schedule.objects.bulk_create(created)
        messages.success(request, f"Generated {len(created)} schedule entries.")
        return redirect('scheduler:timetable-view', semester=sem)
    return render(request, 'scheduler/generate.html')

@login_required
def timetable_view(request, semester):
    qs = (Schedule.objects.filter(semester=semester)
          .select_related('course', 'faculty', 'room', 'timeslot'))
    return render(request, 'scheduler/timetable_view.html', {'schedules': qs, 'semester': semester})

@login_required
@user_passes_test(admin_check)
def edit_cell(request, pk):
    sched = get_object_or_404(Schedule, pk=pk)
    if request.method == 'POST':
        room_id = request.POST.get('room')
        timeslot_id = request.POST.get('timeslot')
        faculty_id = request.POST.get('faculty')

        sched.room = get_object_or_404(Room, pk=room_id)
        sched.timeslot = get_object_or_404(Timeslot, pk=timeslot_id)
        sched.faculty = get_object_or_404(Faculty, pk=faculty_id)

        conflicts = check_conflict(sched, exclude_id=sched.id)
        if conflicts:
            return JsonResponse({'conflicts': conflicts}, status=400)
        sched.save()
        return JsonResponse({'status': 'ok'})

    # GET → return HTML fragment for modal
    return render(request, 'scheduler/edit_cell.html', {
        'sched': sched,
        'rooms': Room.objects.all(),
        'timeslots': Timeslot.objects.all(),
        'faculty': Faculty.objects.all(),
    })