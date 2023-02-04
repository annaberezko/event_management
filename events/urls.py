from django.urls import path

from events.views import EventsAPIView, EventsTypesAPIView

app_name = 'events'

urlpatterns = [
    path('', EventsAPIView.as_view(), name='events-list'),
    path('types/', EventsTypesAPIView.as_view(), name='events-types-list'),
]
