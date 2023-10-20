from .base import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         #'NAME': BASE_DIR / 'db.sqlite3',
#         'NAME': os.path.join(BASE_DIR / 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'localhost',
        'PORT': '5432',
        'USER': get_secret('USER'),
        'PASSWORD': get_secret('PASSWORD'),
        'NAME': get_secret('DB_NAME'),
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# STATIC_URL = '/static/'
# STATICFILES_DIRS =  (BASE_DIR.child('static'), )

# MEDIA_URL = '/media/'
# MEDIA_ROOT = [BASE_DIR.child('media')]


STATIC_URL = '/static/'
STATICFILES_DIRS = [ BASE_DIR / "static", ]
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

