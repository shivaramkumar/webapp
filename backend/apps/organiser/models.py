"""
This module defines the data models for the Event in the application.

Classes:
    Event: Represents an event with a title, description, start time, and end time.

    Task: Represents a task with a description and due date.

    # TODO: Add more models as needed. Update the documentation for each model after updation!
"""

from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=200, default='', help_text='Title of the event')
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    # other fields...

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
        default_related_name = 'events'

    def __str__(self) -> str:
        return self.title


class Task(models.Model):
    description = models.TextField()
    due_date = models.DateField()

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        default_related_name = 'tasks'

    def __str__(self) -> str:
        return self.description

    # other fields...
