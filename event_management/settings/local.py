from .base import *
from decouple import config

DEBUG = config('DEBUG', default=True)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / config('DB_NAME', default=''),
    }
}
