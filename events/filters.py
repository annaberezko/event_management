from django_filters.rest_framework import FilterSet, CharFilter, filters


class EventsFilter(FilterSet):
    """
    Events list filtering by:
    event_type=<event_type.name>
    timestamp_after=<datetime> and timestamp_before=<datetime>
    """
    event_type = CharFilter(field_name='event_type__name')
    timestamp = filters.DateTimeFromToRangeFilter()
