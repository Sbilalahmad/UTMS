from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Department, Course, Faculty, Room, Timeslot

def admin_check(user):
    return user.is_authenticated and user.role == 'admin'
class DepartmentListView(ListView): 
    model = Department
class DepartmentCreateView(CreateView):
    model = Department; fields = 'all'; success_url = reverse_lazy('core:department-list')
class DepartmentUpdateView(UpdateView):
    model = Department; fields = 'all'; success_url = reverse_lazy('core:department-list')
class DepartmentDeleteView(DeleteView):
    model = Department; success_url = reverse_lazy('core:department-list')

# ----------------  COURSE  ----------------
@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(admin_check), name='dispatch')
class CourseListView(ListView):
    model = Course
    template_name = 'core/course_list.html'
    context_object_name = 'courses'

@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(admin_check), name='dispatch')
class CourseCreateView(CreateView):
    model = Course
    fields = ['name', 'code', 'credits', 'department']
    template_name = 'core/course_form.html'
    success_url = reverse_lazy('core:course-list')

@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(admin_check), name='dispatch')
class CourseUpdateView(UpdateView):
    model = Course
    fields = ['name', 'code', 'credits', 'department']
    template_name = 'core/course_form.html'
    success_url = reverse_lazy('core:course-list')

@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(admin_check), name='dispatch')
class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'core/course_confirm_delete.html'
    success_url = reverse_lazy('core:course-list')


# ----------------  FACULTY  ----------------
@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(admin_check), name='dispatch')
class FacultyListView(ListView):
    model = Faculty
    template_name = 'core/faculty_list.html'
    context_object_name = 'faculty_list'

class FacultyCreateView(CreateView):
    model = Faculty
    fields = ['user', 'name', 'email', 'department', 'availability']
    template_name = 'core/faculty_form.html'
    success_url = reverse_lazy('core:faculty-list')

class FacultyUpdateView(UpdateView):
    model = Faculty
    fields = ['user', 'name', 'email', 'department', 'availability']
    template_name = 'core/faculty_form.html'
    success_url = reverse_lazy('core:faculty-list')

class FacultyDeleteView(DeleteView):
    model = Faculty
    template_name = 'core/faculty_confirm_delete.html'
    success_url = reverse_lazy('core:faculty-list')


# ----------------  ROOM  ----------------
@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(admin_check), name='dispatch')
class RoomListView(ListView):
    model = Room
    template_name = 'core/room_list.html'
    context_object_name = 'rooms'

class RoomCreateView(CreateView):
    model = Room
    fields = ['name', 'capacity', 'type']
    template_name = 'core/room_form.html'
    success_url = reverse_lazy('core:room-list')

class RoomUpdateView(UpdateView):
    model = Room
    fields = ['name', 'capacity', 'type']
    template_name = 'core/room_form.html'
    success_url = reverse_lazy('core:room-list')

class RoomDeleteView(DeleteView):
    model = Room
    template_name = 'core/room_confirm_delete.html'
    success_url = reverse_lazy('core:room-list')


# ----------------  TIMESLOT  ----------------
@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(admin_check), name='dispatch')
class TimeslotListView(ListView):
    model = Timeslot
    template_name = 'core/timeslot_list.html'
    context_object_name = 'timeslots'

class TimeslotCreateView(CreateView):
    model = Timeslot
    fields = ['day_of_week', 'start_time', 'end_time']
    template_name = 'core/timeslot_form.html'
    success_url = reverse_lazy('core:timeslot-list')

class TimeslotUpdateView(UpdateView):
    model = Timeslot
    fields = ['day_of_week', 'start_time', 'end_time']
    template_name = 'core/timeslot_form.html'
    success_url = reverse_lazy('core:timeslot-list')

class TimeslotDeleteView(DeleteView):
    model = Timeslot
    template_name = 'core/timeslot_confirm_delete.html'
    success_url = reverse_lazy('core:timeslot-list')