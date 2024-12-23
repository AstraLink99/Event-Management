from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('events/', views.event_list, name='event_list'),  # List all events
    path('events/add/', views.add_event, name='add_event'),  # Add a new event
    path('events/<int:event_id>/edit/', views.edit_event, name='edit_event'),  # Edit an event
    path('events/<int:event_id>/delete/', views.delete_event, name='delete_event'),  # Delete an event
    path('attendees/', views.attendee_list, name='attendee_list'),  # List all attendees
    path('attendees/add/', views.add_attendee, name='add_attendee'),  # Add a new attendee
    path('attendees/<int:attendee_id>/delete/', views.delete_attendee, name='delete_attendee'),
    path('tasks/', views.task_list, name='task_list'),  # List tasks
    path('tasks/add/', views.add_task, name='add_task'),
    path('tasks/<int:task_id>/update/', views.update_task, name='update_task'),  # Update a task
    path('calendar/events/', views.calendar_events, name='calendar_events'),
    path('calendar/', views.calendar, name='calendar'),
]
