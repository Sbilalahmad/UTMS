from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    # departments
    path('departments/', views.DepartmentListView.as_view(), name='department-list'),
    path('departments/add/', views.DepartmentCreateView.as_view(), name='department-add'),
    path('departments/<int:pk>/edit/', views.DepartmentUpdateView.as_view(), name='department-edit'),
    path('departments/<int:pk>/delete/', views.DepartmentDeleteView.as_view(), name='department-delete'),

    # courses
    path('courses/', views.CourseListView.as_view(), name='course-list'),
    path('courses/add/', views.CourseCreateView.as_view(), name='course-add'),
    path('courses/<int:pk>/edit/', views.CourseUpdateView.as_view(), name='course-edit'),
    path('courses/<int:pk>/delete/', views.CourseDeleteView.as_view(), name='course-delete'),

    # faculty
    path('faculty/', views.FacultyListView.as_view(), name='faculty-list'),
    path('faculty/add/', views.FacultyCreateView.as_view(), name='faculty-add'),
    path('faculty/<int:pk>/edit/', views.FacultyUpdateView.as_view(), name='faculty-edit'),
    path('faculty/<int:pk>/delete/', views.FacultyDeleteView.as_view(), name='faculty-delete'),

    # rooms
    path('rooms/', views.RoomListView.as_view(), name='room-list'),
    path('rooms/add/', views.RoomCreateView.as_view(), name='room-add'),
    path('rooms/<int:pk>/edit/', views.RoomUpdateView.as_view(), name='room-edit'),
    path('rooms/<int:pk>/delete/', views.RoomDeleteView.as_view(), name='room-delete'),

    # timeslots
    path('timeslots/', views.TimeslotListView.as_view(), name='timeslot-list'),
    path('timeslots/add/', views.TimeslotCreateView.as_view(), name='timeslot-add'),
    path('timeslots/<int:pk>/edit/', views.TimeslotUpdateView.as_view(), name='timeslot-edit'),
    path('timeslots/<int:pk>/delete/', views.TimeslotDeleteView.as_view(), name='timeslot-delete'),
]