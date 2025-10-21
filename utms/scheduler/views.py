from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Schedule
from .algorithm import run_scheduler

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