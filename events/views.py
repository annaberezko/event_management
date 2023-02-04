from rest_framework import generics

from events.models import Event, EventType
from events.serializers import EventSerializer


class EventsAPIView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def perform_create(self, serializer):
        user = self.request.user
        event_data = dict(serializer.validated_data)
        event_type = event_data['event_type']
        del event_data['event_type']

        event, _ = EventType.objects.get_or_create(name__iexact=event_type)
        Event.objects.create(**event_data, event_type=event, user=user)
