"""
Django settings for cuiquer project.

Generated by 'django-admin startproject' using Django 1.9.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import sys
from configurations import Configuration

TESTING = 'test' in sys.argv


class Common(Configuration):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = '8ek1arbfsu_a4!=ptl8r-ulmq5q8jt$io%&)bfx+c$u*lr3ibn'

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    ALLOWED_HOSTS = []

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django_nose',
        'localflavor',
        'landing',
        'clientes',
        'profesionales',
        'perfiles',
        'django_extensions',
        'djcelery_email',
    ]

    MIDDLEWARE_CLASSES = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'rollbar.contrib.django.middleware.RollbarNotifierMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware',
    ]

    ROOT_URLCONF = 'cuiquer.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [
                os.path.join(BASE_DIR, 'landing/templates'),
                os.path.join(BASE_DIR, 'profesionales/templates'),
                os.path.join(BASE_DIR, 'clientes/templates'),
                os.path.join(BASE_DIR, 'correos/templates'),
            ],
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
                'loaders': [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ]
            },
        },
    ]
    WSGI_APPLICATION = 'cuiquer.wsgi.application'

    # Password validation
    # https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
    # https://docs.djangoproject.com/en/1.9/topics/i18n/
    LANGUAGE_CODE = 'es'
    TIME_ZONE = 'UTC'
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True

    # Staticfiles
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

    # Mediafiles
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')

    TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
    NOSE_ARGS = [
        '--with-coverage',
        '--cover-package=landing, clientes, profesionales',
        '--cover-html',
        '--cover-inclusive',
    ]

    AUTH_USER_MODEL = 'perfiles.Usuario'

    # Redes Sociales
    FACEBOOK = 'https://www.facebook.com/cuiquer/'
    TWITTER = 'https://twitter.com/Cuiquer_es'
    INSTAGRAM = 'https://www.instagram.com/cuiquer/'


class Dev(Common):
    DEBUG = True
    # Database
    # https://docs.djangoproject.com/en/1.9/ref/settings/#databases
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(Common.BASE_DIR, 'db.sqlite3'),
        }
    }
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


class Prod(Common):
    # Database
    # https://docs.djangoproject.com/en/1.9/ref/settings/#databases
    import dj_database_url
    Common.DATABASES['default'] = dj_database_url.config()

    ALLOWED_HOSTS = [".herokuapp.com", ".researchthroughdesign.org"]
    DEBUG = False

    EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'
    EMAIL_HOST = 'mail.privateemail.com'
    EMAIL_PORT = 465
    EMAIL_HOST_USER = 'hello@cuiquer.com'
    EMAIL_HOST_PASSWORD = 'cuiquer123'
    EMAIL_USE_TLS = True

    ROLLBAR = {
        'access_token': 'b5781909e8464502bade1b1127406ae1',
        'environment': 'development' if DEBUG else 'production',
        'root': Common.BASE_DIR,
    }
    import rollbar
    rollbar.init(**ROLLBAR)
