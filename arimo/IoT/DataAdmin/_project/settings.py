"""
Django settings for project.

Generated by 'django-admin startproject' using Django 1.11.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""


import os
from ruamel import yaml
import six
import sys


# check if running on Linux cluster or local Mac
_ON_LINUX_CLUSTER = sys.platform.startswith('linux')


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
_PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

BASE_DIR = os.path.dirname(_PROJECT_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = not _ON_LINUX_CLUSTER


INTERNAL_IPS = ['127.0.0.1']


ALLOWED_HOSTS = \
    ['.arimo.com', '.elasticbeanstalk.com'] \
    if _ON_LINUX_CLUSTER \
    else ['127.0.0.1', 'localhost']


# Application definition

INSTALLED_APPS = [
    # Django-AutoComplete-Light: add to INSTALLED_APPS BEFORE django.contrib.admin
    'dal',
    'dal_select2',

    'dal_contenttypes',
    'dal_genericm2m',
    'dal_genericm2m_queryset_sequence',
    'dal_gm2m',
    'dal_gm2m_queryset_sequence',
    'dal_queryset_sequence',
    'dal_select2_queryset_sequence',
    'dal_select2_tagging',
    'dal_select2_taggit',

    # 'grappelli',

    'django_extensions',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework_filters',
    'crispy_forms',

    'debug_toolbar',
    'silk',

    'arimo.IoT.DataAdmin.base',
    'arimo.IoT.DataAdmin.PredMaint'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'debug_toolbar.middleware.DebugToolbarMiddleware',
        # You should include the Debug Toolbar middleware as early as possible in the list.
        # However, it must come after any other middleware that encodes the response's content, such as GZipMiddleware
    'silk.middleware.SilkyMiddleware'
]

ROOT_URLCONF = 'arimo.IoT.DataAdmin._project.urls'

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
                'django.contrib.messages.context_processors.messages'
            ],
        },
    },
]

WSGI_APPLICATION = 'arimo.IoT.DataAdmin._project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

_DB_DETAILS_FILE_NAME = 'db.yaml'
_DB_DETAILS_FILE_PATH = os.path.join(_PROJECT_DIR, _DB_DETAILS_FILE_NAME)

_db_details = yaml.safe_load(stream=open(_DB_DETAILS_FILE_PATH, 'r'))['db']['admin']

DATABASES = \
    dict(default=
        dict(ENGINE='django.db.backends.postgresql', PORT='5432',
             HOST=_db_details['host'], NAME=_db_details['db_name'],
             USER=_db_details['user'], PASSWORD=_db_details['password']))


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'


# REST Framework settings
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.RemoteUserAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],

    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],

    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,   # 100

    'DEFAULT_FILTER_BACKENDS': [
        'rest_framework_filters.backends.RestFrameworkFilterBackend'
    ]
    if six.PY3
    else []
}
