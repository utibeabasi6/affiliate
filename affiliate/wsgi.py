"""
WSGI config for affiliate project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
from whitenoise import WhiteNoise

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'affiliate.settings')

application = get_wsgi_application()
application = WhiteNoise(application, root= BASE_DIR / 'media', prefix='/media/')