from datetime import datetime

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status

from rest_framework.test import APITestCase, APIClient

from events.models import EventType, Event

User = get_user_model()


class EventsAPIViewAPIViewTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='super', password='strong')
        self.event = EventType.objects.create(name="meeting")
        self.url = reverse('v1.0:events:events-list')

        res = self.client.post(reverse('v1.0:obtain_auth_token'), {'username': 'super', 'password': 'strong'})
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {res.data['token']}")

        self.data = {
            "event_type": "Party",
            "info": {"place": "Street Name, 1", "Some information field": "..."},
            "timestamp": "2023-11-23 10:00"
        }

    def test_create_new_event_for_un_authenticated_client(self):
        client = APIClient()
        response = client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_new_event_empty_data_error(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['event_type'][0], 'This field is required.')
        self.assertEqual(response.data['info'][0], 'This field is required.')
        self.assertEqual(response.data['timestamp'][0], 'This field is required.')

    def test_create_new_event_empty_event_type_error(self):
        del self.data['event_type']
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['event_type'][0], 'This field is required.')

    def test_create_new_event_empty_info_error(self):
        del self.data['info']
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['info'][0], 'This field is required.')

    def test_create_new_event_empty_timestamp_error(self):
        del self.data['timestamp']
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['timestamp'][0], 'This field is required.')

    def test_create_new_event_long_event_type_more_than_256_characters_error(self):
        self.data['event_type'] = "qwertyqwertyqwertyqwertyqwertyqwertyqwertyqwertyqwertyqwertyqwertyqwertyqwerty" \
                                  "qwertyqwertyqwertyqwertyqwertyqwertyqwertyqwertyqwertyqwertyqwertyqwertyqwerty" \
                                  "qwertyqwertyqwertyqwertyqwertyqwertyqwertyqwertyqwertyqwertyqwertyqwertyqwerty" \
                                  "qwertyqwertyqwertyqwertyqwertyqwerty"
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue(response.data['event_type'])

    def test_create_new_event_timestamp_invalid_format_error(self):
        self.data['timestamp'] = 1
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue(response.data['timestamp'])

    def test_create_new_event_success(self):
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        last_event_type = EventType.objects.last()
        self.assertEqual(last_event_type.name, 'party')
        last_event = Event.objects.last()
        self.assertEqual(last_event.created_at.strftime('%Y-%m-%d'), f"{datetime.now():%Y-%m-%d}")

    def test_create_new_event_is_not_case_sensitive_success(self):
        self.data['event_type'] = 'MeetinG'
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(EventType.objects.all().count(), 1)
