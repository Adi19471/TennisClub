"""
WSGI config for TENNIS_CLUB_MANAGEMNET_SYSTEM project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
from dj_static import Cling
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TENNIS_CLUB_MANAGEMNET_SYSTEM.settings')

application = Cling(get_wsgi_application())
