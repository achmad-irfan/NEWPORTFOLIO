from .base import *

DEBUG= True

ALLOWED_HOSTS = []




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'newweb',
        'USER': 'root',
        'PASSWORD': 'dave',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

STATIC_URL = "static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')]