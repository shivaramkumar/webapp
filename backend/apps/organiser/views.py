from django.views import generic

from .models import Event


class EventListView(generic.ListView):
    model = Event


class EventCreateView(generic.CreateView):
    model = Event
    fields = ['title', 'description', 'start_time', 'end_time']


# similar views for Task and other models...
