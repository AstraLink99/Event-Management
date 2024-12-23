from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Event
from .forms import EventForm
from .models import Task
from .forms import TaskForm
from .models import Attendee
from .forms import AttendeeForm
from django.urls import reverse_lazy
from django.db.models import Count, Q
from django.http import JsonResponse

def home(request):
    return render(request, 'EventApp/home.html')

@login_required
def attendee_list(request):
    attendees = Attendee.objects.all()
    return render(request, 'EventApp/attendee_list.html', {'attendees': attendees})

@login_required
def add_attendee(request):
    if request.method == 'POST':
        form = AttendeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendee_list')
    else:
        form = AttendeeForm()
    return render(request, 'EventApp/attendee_form.html', {'form': form})

@login_required
def delete_attendee(request, attendee_id):
    attendee = get_object_or_404(Attendee, id=attendee_id)
    if request.method == 'POST':
        attendee.delete()
        return redirect('attendee_list')
    return render(request, 'EventApp/attendee_confirm_delete.html', {'attendee': attendee})

# View to list all events
@login_required
def event_list(request):
    events = Event.objects.annotate(
        total_tasks=Count('tasks'),
        completed_tasks=Count('tasks', filter=Q(tasks__status='Completed'))
    )
    return render(request, 'EventApp/event_list.html', {'events': events})

# View to add a new event
@login_required
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        attendees = Attendee.objects.all()  
        if form.is_valid():
            event = form.save()
            assigned_attendees = request.POST.getlist('attendees')
            event.attendees.set(assigned_attendees)  
            return redirect('event_list')
    else:
        form = EventForm()
        attendees = Attendee.objects.all()  

    return render(request, 'EventApp/event_form.html', {'form': form, 'attendees': attendees})

# View to edit an event
@login_required
def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save()
            attendees = request.POST.getlist('attendees')
            event.attendees.set(attendees)  
            return redirect('event_list')
    else:
        form = EventForm(instance=event)
        attendees = Attendee.objects.all()
    return render(request, 'EventApp/event_form.html', {'form': form, 'attendees': attendees})

# View to delete an event
@login_required
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')
    return render(request, 'EventApp/event_confirm_delete.html', {'event': event})

@login_required
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'EventApp/task_list.html', {'tasks': tasks})

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'EventApp/task_form.html', {'form': form})

@login_required
def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'EventApp/task_form.html', {'form': form})

def calendar_events(request):
    events = Event.objects.all()
    events_list = [
        {
            "title": event.name,
            "start": event.date.isoformat(),  # Convert to ISO format
            "description": event.description,
        }
        for event in events
    ]
    return JsonResponse(events_list, safe=False)

def calendar(request):
    return render(request, 'EventApp/calendar.html')

