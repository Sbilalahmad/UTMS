from django.urls import path
from . import views
app_name = 'scheduler'
urlpatterns = [
    path('generate/', views.generate_timetable, name='generate'),
    path('view/<str:semester>/', views.timetable_view, name='timetable-view'),
    path('edit/<int:pk>/', views.edit_cell, name='edit-cell'),
]