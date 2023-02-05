from django.contrib import admin
from django.urls import path, include

from rest_framework.authtoken import views

from .yasg import urlpatterns as doc_urls

admin.site.site_header = 'Event management system'
admin.site.site_title = 'Main administrator'

v1_0_patterns = [
    path('api-token-auth/', views.obtain_auth_token, name='obtain_auth_token'),
    path('events/', include('events.urls')),
]

v1_0_patterns += doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1.0/', include((v1_0_patterns, 'v1.0'), namespace='v1.0')),
]


