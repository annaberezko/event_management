from django.urls import path

from events.views import EventsAPIView

app_name = 'events'

urlpatterns = [
    path('', EventsAPIView.as_view(), name='events-list'),
]
