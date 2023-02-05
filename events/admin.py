from django.contrib import admin
from django_admin_listfilter_dropdown.filters import DropdownFilter

from rangefilter.filters import DateTimeRangeFilter

from events.models import Event, EventType


admin.site.register(EventType)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

    list_display = ['user', 'event_type', 'timestamp', 'created_at']
    list_filter = (
            ('event_type__name', DropdownFilter),
            ('timestamp', DateTimeRangeFilter),
        )
