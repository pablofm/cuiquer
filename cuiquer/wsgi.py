"""
WSGI config for gettingstarted project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from configurations import importer
from whitenoise.django import DjangoWhiteNoise


importer.install()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cuiquer.settings")
application = get_wsgi_application()
application = DjangoWhiteNoise(application)
