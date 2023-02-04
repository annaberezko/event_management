from django.contrib import admin
from django.urls import path, include

from rest_framework.authtoken import views

v1_0_patterns = [
    path('api-token-auth/', views.obtain_auth_token, name='obtain_auth_token'),
    path('events/', include('events.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1.0/', include((v1_0_patterns, 'v1.0'), namespace='v1.0')),
]
