from django.db import models

from django.db import models

# Event Model
class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    date = models.DateField()
    attendees = models.ManyToManyField('Attendee', related_name='events', blank=True)

    def __str__(self):
        return self.name

# Attendee Model
class Attendee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

# Task Model
class Task(models.Model):
    PENDING = 'Pending'
    COMPLETED = 'Completed'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (COMPLETED, 'Completed'),
    ]

    name = models.CharField(max_length=255)
    deadline = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)
    assigned_attendee = models.ForeignKey(Attendee, on_delete=models.SET_NULL, null=True, related_name='tasks')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return f"{self.name} - {self.status}"

