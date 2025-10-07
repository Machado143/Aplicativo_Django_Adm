"""
ASGI config for aula03 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from servestatic import ServeStaticASGI
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aula03.settings')

application = get_asgi_application()
application = ServeStaticASGI(application)
application.add_files(settings.MEDIA_ROOT, settings.MEDIA_URL)
