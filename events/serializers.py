from rest_framework import serializers

from events.models import Event


class EventSerializer(serializers.ModelSerializer):
    event_type = serializers.CharField(max_length=256)

    class Meta:
        model = Event
        fields = ('event_type', 'info', 'timestamp')
