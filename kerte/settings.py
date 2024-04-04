"""
Django settings for kerte project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

import os
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG")
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True

STATIC_ROOT="STATICFILES"

ALLOWED_HOSTS = ['127.0.0.1','.vercel.app','*']


# Application definition

INSTALLED_APPS = [
    'grappelli.dashboard',
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'LandingPages', 
    'service',
    'storages',
    'pwa',
    'django_cleanup.apps.CleanupConfig',
    'guardian',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django_session_timeout.middleware.SessionTimeoutMiddleware',
]

ROOT_URLCONF = 'kerte.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'kerte.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

if DEBUG == "False":
    DATABASES = {
        'default': {
            'ENGINE' : 'django.db.backends.postgresql_psycopg2',
            'NAME' : os.getenv("POSTGRES_DATABASE"),
            'USER' : os.getenv("POSTGRES_USER"),
            'PASSWORD':os.getenv("POSTGRES_PASSWORD"),
            'HOST':os.getenv("POSTGRES_HOST"),
            "PORT":os.getenv("POSTGRES_PORT"),
        }
    }
    #AWS
    AWS_ACCESS_KEY_ID=os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY=os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME=os.getenv("AWS_STORAGE_BUCKET_NAME")
    AWS_S3_CUSTOM_DOMAIN='%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
    AWS_S3_FILE_OVERWRITE=False
    AWS_S3_CUSTOM_DOMAIN=os.getenv("AWS_S3_CUSTOM_DOMAIN")

    STORAGES={
        #for media file storage
        "default":{
            "BACKEND":"storages.backends.s3boto3.S3StaticStorage",
        },

        #for css/js
        "staticfiles":{
            "BACKEND":"storages.backends.s3boto3.S3StaticStorage",
        }
    }

else:
    DATABASES = {
        'default': {
            'ENGINE' : 'django.db.backends.postgresql_psycopg2',
            'NAME' : os.getenv("DB_DATABASE"),
            'USER' : os.getenv("DB_USER"),
            'PASSWORD':os.getenv("DB_PASSWORD"),
            'HOST':os.getenv("DB_HOST"),
            'PORT':os.getenv("DB_PORT"),
        }
    }

    STATICFILES_DIRS=[
        BASE_DIR / "node_modules",
    ]


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

'''DJANGO GRAPPELLLI'''

GRAPPELLI_INDEX_DASHBOARD ='kerte.dashboard.CustomIndexDashboard'

'''DJANGO-GUARDIAN'''

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', # this is default
    'guardian.backends.ObjectPermissionBackend',
)

'''USER MODEL'''
AUTH_USER_MODEL='service.Base_user'


'''SESSION EXPIRATION CONF'''
SESSION_EXPIRE_AFTER_LAST_ACTIVITY=True
SESSION_EXPIRE_SECONDS=730
SESSION_EXPIRE_AFTER_LAST_ACTIVITY_GRACE_PERIOD=60
SESSION_TIMEOUT_REDIRECT='/accounts/signin/'

'''PWA CONFIGURATION'''

PWA_APP_NAME="kerte"
PWA_APP_DESCRIPTION="app"
PWA_APP_THEME_COLOR="#1ba0e3"
PWA_APP_BACKGROUND_COLOR="#1ba0e3"
PWA_APP_DISPLAY="standalone"
PWA_APP_SCOPE='/'
PWA_APP_ORIENTATION="Portrait"
PWA_APP_START_URL='/'
PWA_APP_STATUS_BAR_COLOR='default'
PWA_APP_ICONS=[
    {
        'src':'',
        'sizes':'160x160'
    }
]

PWA_APP_ICONS_APPLE=[
    {
        'src':'',
        'size':'160x160'
    }
]

PWA_APP_SPLASH_SCREEN=[
    {
        'src':'',
        'media':'(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)'
    }
]
PWA_APP_DIR='ltr'
PWA_APP_LANG='en-US'
PWA_SERVICE_WORKER_PATH=os.path.join(STATIC_ROOT,'javascript','serviceworker.js')