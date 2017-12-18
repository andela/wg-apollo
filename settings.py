#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Use 'DEBUG = True' to get more details for server errors
from wger.settings_global import *

DEBUG = True
TEMPLATES[0]['OPTIONS']['debug'] = True

ADMINS = (
    ('Your name', 'your_email@example.com'),
)
MANAGERS = ADMINS


DATABASES = {
    'default': {
        'ENGINE': os.getenv("ENGINE"),
        'NAME': os.getenv("DB_NAME"),
        'USER': os.getenv("DB_USER"),
        'PASSWORD': os.getenv("DB_USER_PASSWORD"),
        'HOST': os.getenv("HOST"),
        'PORT': os.getenv("DB_PORT_NUMBER"),
        'TEST': {'CHARSET': 'UTF8'}
    }
}

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'ee8sodm&=ojl2aazl$vum2=w3n5_s+am#wk9sc%ue&4v&&5f31'

# Your reCaptcha keys
RECAPTCHA_PUBLIC_KEY = ''
RECAPTCHA_PRIVATE_KEY = ''
NOCAPTCHA = True

# The site's URL (e.g. http://www.my-local-gym.com or http://localhost:8000)
# This is needed for uploaded files and images (exercise images, etc.) to be
# properly served.
SITE_URL = 'http://localhost:8000'

# Path to uploaded files
# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Allow all hosts to access the application. Change if used in production.
ALLOWED_HOSTS = '*'

# This might be a good idea if you setup memcached
# SESSION_ENGINE = "django.contrib.sessions.backends.cache"

# Configure a real backend in production
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Sender address used for sent emails
WGER_SETTINGS['EMAIL_FROM'] = 'wger Workout Manager <wger@example.com>'

# Your twitter handle, if you have one for this instance.
# WGER_SETTINGS['TWITTER'] = ''

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'wger', 'core', 'static'),
    os.path.join(BASE_DIR, 'wger', 'exercises', 'static'),
    os.path.join(BASE_DIR, 'wger', 'nutrition', 'static'),
    os.path.join(BASE_DIR, 'wger', 'weight', 'static'),
)

