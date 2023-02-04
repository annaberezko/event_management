from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from events.filters import EventsFilter
from events.models import Event, EventType
from events.serializers import EventSerializer, EventTypeSerializer


class EventsAPIView(generics.ListCreateAPIView):
    queryset = Event.objects.select_related('event_type').all()
    serializer_class = EventSerializer

    filter_backends = (DjangoFilterBackend, )
    filterset_class = EventsFilter

    def get_queryset(self):
        if self.request.method == 'GET':
            return Event.objects.select_related('event_type').filter(user=self.request.user)
        return super().get_queryset()

    def perform_create(self, serializer):
        user = self.request.user
        event_data = dict(serializer.validated_data)
        event_type = event_data['event_type'].lower()
        del event_data['event_type']

        event, _ = EventType.objects.get_or_create(name=event_type)
        Event.objects.create(**event_data, event_type=event, user=user)


class EventsTypesAPIView(generics.ListAPIView):
    queryset = EventType.objects.all()
    serializer_class = EventTypeSerializer
